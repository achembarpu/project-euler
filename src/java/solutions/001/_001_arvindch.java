// Author: Arvind Chembarpu
// Email: achembarpu@gmail.com

public class _001_arvindch {

	public static void main(String[] args) {
		int n, giv_lim = 1000, req_sum = 0;
		
		for(n=0; n<giv_lim; n++) {
			
			if(n%3==0 || n%5==0) {
				req_sum += n;
			}
		}
		
		System.out.println(req_sum);
	}

}
