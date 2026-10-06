# LoraLoader|pysssss

## 节点类型

`LoraLoader|pysssss`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `lora_name:COMBO`（1 次）
- `strength_model:FLOAT`（1 次）
- `strength_clip:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（2 次）
- `CLIP:CLIP`（2 次）
- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["小红书极致真人写实—美妆大胸美女_F.1.safetensors", 1, 1.72, "[none]"]`（1 次）
- `[{"image": "loras/FLUX\\F.1优化\\【梵·AIGC】超写实手部摄影_极致逼真美学FLUX模型_极致美学Pro.jpg", "content": "FLUX\\F.1优化\\【梵·AIGC】超写实手部摄影_极致逼真美`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
