---
name: image_to_image_sampler_checkpoint_vae
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9652
common_nodes: [CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/【阡陌】基础图生图 中文提示词自动翻译_1942178643743555586.json, 图片生成/图生图/二次元生成-V1.0_1911766445062090754.json, 图片生成/图生图/图生图 老树开新花 SDXL图生图 极速_2021849030879354881.json, 图片生成/图生图/图生图+CN_Depth+Lora_1777989245395341313.json, 图片生成/图生图/图生图+CN_Depth_1777527452583596033.json, 图片生成/图生图/图生图+LoRA-烟花下的童贞_1976482856375554050.json, 图片生成/图生图/图生图+LoRA_1818199143159365633.json, 图片生成/图生图/图生图+LoRA_2008468367568539650.json, 图片生成/图生图/图生图3D+LoRA_1911301546905403393.json, 图片生成/图生图/毛坯房一键生成_2049031226702438402.json]
source: knowledge_consolidation
---

# image_to_image_sampler_checkpoint_vae

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/【阡陌】基础图生图 中文提示词自动翻译_1942178643743555586.json、图片生成/图生图/二次元生成-V1.0_1911766445062090754.json、图片生成/图生图/图生图 老树开新花 SDXL图生图 极速_2021849030879354881.json、图片生成/图生图/图生图+CN_Depth+Lora_1777989245395341313.json、图片生成/图生图/图生图+CN_Depth_1777527452583596033.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 9/10 个有
- `LoraLoader` —— 9/10 个有
- `RepeatLatentBatch` —— 7/10 个有
- `PreviewImage` —— 4/10 个有
- `ControlNetApplyAdvanced` —— 3/10 个有
- `ControlNetLoader` —— 3/10 个有
- `Zoe-DepthMapPreprocessor` —— 3/10 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/10 个有
- `IPAdapterAdvanced` —— 1/10 个有
- `IPAdapterUnifiedLoader` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `LatentUpscaleBy` —— 1/10 个有
- `M-LSDPreprocessor` —— 1/10 个有
- `PrepImageForClipVision` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 10 | 85% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 10 | 71% |
| 采样算法 | euler_ancestral | - | 10 | 60% |
| 调度器 | normal | - | 10 | 70% |
| 重绘幅度 | 0.53 | 0.4 - 1 | 10 | 74% |
| LoRA 模型强度 | 0.4 | 0.3 - 1 | 9 | 55% |
| LoRA 文本强度 | 1 | 0.3 - 1 | 9 | 72% |
| ControlNet 权重 | 1 | 0.4 - 1 | 3 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，10 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，10 个样本
- 采样算法 最常用 euler_ancestral，10 个样本，一致性 60%
- 调度器 最常用 normal，10 个样本，一致性 70%
- 重绘幅度 中位数 0.53，观测区间 0.4 - 1，10 个样本
- LoRA 模型强度 中位数 0.4，观测区间 0.3 - 1，9 个样本
- LoRA 文本强度 中位数 1，观测区间 0.3 - 1，9 个样本
- ControlNet 权重 中位数 1，观测区间 0.4 - 1，3 个样本
