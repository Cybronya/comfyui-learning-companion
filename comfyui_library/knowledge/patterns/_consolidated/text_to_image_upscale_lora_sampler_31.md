---
name: text_to_image_upscale_lora_sampler_31
type: Text To Image
frequency: 7
level: moderate
coverage: 0.924857
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageScale, ImageUpscaleWithModel, KSampler, LoraLoader, SaveImage, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/ChenkinNoobXL文生图工作流_2091808819218309122.json, 图片生成/文生图/Illustrious+二次元动漫插画工作流_2028299693389783042.json, 图片生成/文生图/SDXL Illustrious 2d cg插画工作流_1977304880945733633.json, 图片生成/文生图/SDXL+Illustrious+二次元动漫插画工作流_2010926888553811969.json, 图片生成/文生图/SDXL+Illustrious+二次元动漫插画工作流_2049309152706568194.json, 图片生成/文生图/【文生图】Illustrious+DPM+++全节点注释_2058772797203247105.json, 图片生成/文生图/【文生图】流光溢彩 · Illustrious五重绘卷_2054181305167958017.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/ChenkinNoobXL文生图工作流_2091808819218309122.json、图片生成/文生图/Illustrious+二次元动漫插画工作流_2028299693389783042.json、图片生成/文生图/SDXL Illustrious 2d cg插画工作流_1977304880945733633.json、图片生成/文生图/SDXL+Illustrious+二次元动漫插画工作流_2010926888553811969.json、图片生成/文生图/SDXL+Illustrious+二次元动漫插画工作流_2049309152706568194.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 5/7 个有
- `easy promptLine` —— 3/7 个有
- `CR Text` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `RH_Translator` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 768 - 1984 | 7 | 57% |
| 高度 | 1216 | 1120 - 1984 | 7 | 79% |
| 采样步数 | 35 | 20 - 35 | 7 | 84% |
| Prompt 约束强度(CFG) | 4 | 4 - 5 | 7 | 90% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 7 | 57% |
| 调度器 | karras | - | 7 | 86% |
| 重绘幅度 | 1 | 0.45 - 1 | 7 | 70% |
| LoRA 模型强度 | 1 | 0.3 - 1 | 7 | 60% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 832，观测区间 768 - 1984，7 个样本
- 高度 中位数 1216，观测区间 1120 - 1984，7 个样本
- 采样步数 中位数 35，观测区间 20 - 35，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 5，7 个样本，取值集中（一致性 90%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，7 个样本，一致性 57%
- 调度器 最常用 karras，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.45 - 1，7 个样本
- LoRA 模型强度 中位数 1，观测区间 0.3 - 1，7 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
