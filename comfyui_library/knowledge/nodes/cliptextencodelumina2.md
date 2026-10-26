# CLIPTextEncodeLumina2

## 节点类型

`CLIPTextEncodeLumina2`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（4 次）
- `system_prompt:COMBO`（4 次）
- `user_prompt:STRING`（4 次）

## 输出

- `CONDITIONING:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["superior", "模糊，低分辨率，像素化，噪点，马赛克，画面撕裂，色彩溢出，色彩暗淡，白平衡失调，曝光过度，曝光不足，人物五官畸形，面部模糊，多手多脚，肢体残缺，比例失调，手指错乱，眼神空洞，皮肤油腻，皮肤斑驳，景色透视错误，建筑`（2 次）
- `["superior", "超清画质，真实，专业街头摄影，细节丰富，面容清晰。\n一名中国美女全身出镜，做出合适的模特站立姿势；面容美丽，皮肤白皙，黑色长发简单盘起；身着中式开叉短旗袍，旗袍至小腿处；上身有白色毛绒披肩，胸口露出，右手拿小圆`（1 次）
- `["superior", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
