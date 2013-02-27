<?php

class IsbnController extends BaseController {

    public function cite($project, $isbn)
    {
        if ($project == "itwiki")
            return $this->isbn($isbn);
        else
            return "Error: Project not found";
    }

    public function isbn($isbn)
    {
        $link = $this->retriveIsbnLink($isbn);
        if (!$link)
            return NULL;
        $rawData = $this->retriveJson($link);
        $data = Array();
        $data["titolo"] = $rawData['volumeInfo']['title'];
        $data["id"] = "ISBN " . $isbn;
        $data["anno"] = date("Y", strtotime($rawData['volumeInfo']['publishedDate']));
        $data["mese"] = $this->mese($rawData['volumeInfo']['publishedDate']);
        $data["giorno"] = date("d", strtotime($rawData['volumeInfo']['publishedDate']));
        $data["coautori"] = $this->autori($rawData['volumeInfo']['authors']);
        $data["editore"] = $rawData['volumeInfo']['publisher'];
        return "{{cita libro | " . $this->implode_with_key($data, "=", " | ") . "}}";
    }

    public function checkIsbn($isbn)
    {
        if ($this->retriveIsbnLink($isbn))
            return 1;
        else
            return 0;
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

    private function mese($data)
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
        $mese = date("m", strtotime($data));
        if (isSet($mese) AND $mese > 0 AND $mese < 13)
            return $mesi[$mese];
        else
            return null;
    }

}
