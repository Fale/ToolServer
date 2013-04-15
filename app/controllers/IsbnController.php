<?php

class IsbnController extends BaseController {

    public function cite($project, $isbn)
    {
        if (method_exists($this, $project))
            return $this->{$project}($isbn);
        else
            return "Error: Project not found";
    }

    public function itwiki($isbn)
    {
        $isbn = $this->cleanISBN($isbn);
        $link = $this->retriveIsbnLink($isbn);
        if (!$link)
            return NULL;
        $rawData = $this->retriveJson($link);
        $data = Array();
        $data["titolo"] = $rawData['volumeInfo']['title'];
        $d = $this->data($rawData);
        if (array_key_exists("anno", $d))
        {
            $data["anno"] = $d["anno"];
            $data["mese"] = $d["mese"];
            $data["giorno"] = $d["giorno"];
        }
        $data["coautori"] = $this->autori($rawData['volumeInfo']['authors']);
        $data["editore"] = $rawData['volumeInfo']['publisher'];
        $data["id"] = "ISBN " . $isbn;
        return "{{cita libro | " . $this->implode_with_key($data, "=", " | ") . "}}";
    }

    public function enwiki($isbn)
    {
        $isbn = $this->cleanISBN($isbn);
        $link = $this->retriveIsbnLink($isbn);
        if (!$link)
            return NULL;
        $rawData = $this->retriveJson($link);
        $data = Array();
        $data["title"] = $rawData['volumeInfo']['title'];
        $data["id"] = "ISBN " . $isbn;
        $data["date"] = $rawData['volumeInfo']['publishedDate'];
        $data["editor-last"] = $rawData['volumeInfo']['publisher'];
        return "{{cite book | " . $this->implode_with_key($data, "=", " | ") . "}}";
    }

    public function checkIsbn($isbn)
    {
        $isbn = $this->cleanISBN($isbn);
        if ($this->retriveIsbnLink($isbn))
            return 1;
        else
            return 0;
    }

    private function cleanISBN($isbn)
    {
        $isbn = str_replace(" ","",$isbn);
        $isbn = str_replace("-","",$isbn);
        return $isbn;
    }

    private function retriveIsbnLink($isbn)
    {
        $json = $this->retriveJson("https://www.googleapis.com/books/v1/volumes?q=isbn:$isbn");
        if (array_key_exists('kind', $json))
            if (array_key_exists('totalItems', $json))
                if ($json['totalItems'] > 0)
                    return $json['items']['0']['selfLink'];
        return NULL;
    }

    private function implode_with_key($assoc, $inglue = '>', $outglue = ',')
    {
        $return = '';
        foreach ($assoc as $tk => $tv) {
            $return .= $outglue . $tk . $inglue . $tv;
        }
        return substr($return, strlen($outglue));
    }

    private function retriveJson($url)
    {
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $result = curl_exec($ch);
        curl_close($ch);
        $rawData = json_decode($result, true);
        return $rawData;
    }

    private function autori($datas)
    {
        foreach ($datas as $key => $data)
            $datas[$key] = "[[" . $data . "]]";
        return implode ("; ", $datas);
    }

    private function data($rawData)
    {
        $d = Array();
        $d["anno"] = date("Y", strtotime($rawData['volumeInfo']['publishedDate']));
        $d["mese"] = $this->mese($rawData['volumeInfo']['publishedDate']);
        $d["giorno"] = date("d", strtotime($rawData['volumeInfo']['publishedDate']));
        if( $d["anno"] == date('Y') && $d["mese"] == $this->mese() && $d["giorno"] == date("d"))
            return Array();
        else
            return $d;
    }

    private function mese($data = null)
    {
        $mesi = Array(
            '01' => "gennaio",
            '02' => "febbraio",
            '03' => "marzo",
            '04' => "aprile",
            '05' => "maggio",
            '06' => "giugno",
            '07' => "luglio",
            '08' => "agosto",
            '09' => "settembre",
            '10' => "ottobre",
            '11' => "novembre",
            '12' => "dicembre"
        );
        if ($data)
            $mese = date("m", strtotime($data));
        else
            $mese = date("m");
        if (isSet($mese) AND $mese > 0 AND $mese < 13)
            return $mesi[$mese];
        else
            return null;
    }

}
