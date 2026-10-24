---
name: unknown_workflow_lora_sampler_unet_179
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7785
common_nodes: [CLIPLoader, JjkText, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, QwenImage21Cache, SamplerCustom, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/lora测试 _ qwen_ image_2.1_turbo_bf16_2109473571918667777.json, 图片生成/图生图/抠图_qwen_image_2.1_2110551361774510081.json, "图片生成/图生图/移除遮挡物体 抠图 透明背景 qwen image Image Cutout, Transparen_2112712324380454914.json", 数字人/数字人/QwenImage2.1 高清改图工作流_2110163424536784897.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_179

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/lora测试 _ qwen_ image_2.1_turbo_bf16_2109473571918667777.json、图片生成/图生图/抠图_qwen_image_2.1_2110551361774510081.json、图片生成/图生图/移除遮挡物体 抠图 透明背景 qwen image Image Cutout, Transparen_2112712324380454914.json、数字人/数字人/QwenImage2.1 高清改图工作流_2110163424536784897.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `QwenImage21Cache`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `Int` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
