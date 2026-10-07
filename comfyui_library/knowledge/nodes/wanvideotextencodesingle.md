# WanVideoTextEncodeSingle

## 节点类型

`WanVideoTextEncodeSingle`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `t5:WANTEXTENCODER`（4 次）
- `model_to_offload:WANVIDEOMODEL`（4 次）
- `prompt:STRING`（2 次）

## 输出

- `text_embeds:WANVIDEOTEXTEMBEDS`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，`（2 次）
- `["一个女孩在滑滑板", true]`（1 次）
- `["延时镜头焦点锁定中央静立的少女，她身着素净衣裙，目光沉静望向远方。站在繁华上海街心，周围飞驰的车流化为连绵绚烂的彩色光轨，如液态星河环绕其身侧，行人与灯光拖曳出朦胧虚影。强烈的动静对比中，少女成为喧嚣洪流里唯一的静止坐标。氛围呈现都市迷`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
