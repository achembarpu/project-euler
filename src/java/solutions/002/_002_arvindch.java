public class _002_arvindch {

	public static void main(String[] args) {
		int a=0, b=1, c=1, giv_lim=4000000, req_sum=0;
		
		while(c < giv_lim) {
			
			if(c%2==0) {
				req_sum += c;
			}
			
			c = a + b;
			a = b;
			b = c;
		}
		
		System.out.println(req_sum);
	}

}
