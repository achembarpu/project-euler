public class _004_arvindch {

    public static void main(String[] args) {
        int p=0, giv_low=100, giv_high=1000, req_num=0;

        for(int a=giv_low; a<giv_high; a++) {
            for(int b=a; b<giv_high; b++) {

                p = a * b;
                if(p>req_num) {
                    String s = Integer.toString(p);
                    String rs = new StringBuffer(s).reverse().toString();

                    if(s.equals(rs))
                        req_num = p;
                }
            }
        }

        System.out.println(req_num);
    }

}
