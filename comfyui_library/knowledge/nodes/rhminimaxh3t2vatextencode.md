# RHMiniMaxH3T2VATextEncode

## 节点类型

`RHMiniMaxH3T2VATextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `h3_text_encoder:MINIMAX_H3_TEXT_ENCODER`（2 次）
- `prompt:STRING`（2 次）

## 输出

- `conditioning:MINIMAX_H3_CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["清晨的海边旅行短片。镜头一：航拍蔚蓝海岸，海浪拍打白色沙滩。镜头二：切换到一位白裙女孩赤脚沿海岸奔跑，长发和裙摆随风飘动。镜头三：人物停下脚步，在夕阳光线中回头微笑。画面转场流畅，生成连续海浪声、脚步声、海风声和逐渐增强的浪漫音乐。"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
