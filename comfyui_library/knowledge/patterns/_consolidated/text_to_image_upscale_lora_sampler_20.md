---
name: text_to_image_upscale_lora_sampler_20
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8948
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageScale, ImageUpscaleWithModel, KSampler, LoraLoader, SaveImage, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/1977304880945733633.json, 图片生成/文生图/ChenkinNoobXL文生图工作流_2091808819218309122.json, 图片生成/文生图/SDXL+Illustrious+二次元动漫插画工作流_2010926888553811969.json, 图片生成/文生图/【文生图】Illustrious+DPM+++全节点注释_2058772797203247105.json, 图片生成/文生图/【文生图】流光溢彩 · Illustrious五重绘卷_2054181305167958017.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1977304880945733633.json、图片生成/文生图/ChenkinNoobXL文生图工作流_2091808819218309122.json、图片生成/文生图/SDXL+Illustrious+二次元动漫插画工作流_2010926888553811969.json、图片生成/文生图/【文生图】Illustrious+DPM+++全节点注释_2058772797203247105.json、图片生成/文生图/【文生图】流光溢彩 · Illustrious五重绘卷_2054181305167958017.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
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
- `VAEDecode` —— 3/5 个有
- `CR Text` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `MuyeTextEditOutput` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 768 - 1984 | 5 | 55% |
| 高度 | 1216 | 1120 - 1344 | 5 | 94% |
| LoRA 模型强度 | 1 | 0.3 - 1 | 5 | 52% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 34 | 20 - 35 | 5 | 81% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 5 | 5 | 90% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 5 | 40% |
| 调度器 | karras | - | 5 | 80% |
| 重绘幅度 | 0.55 | 0.45 - 1 | 5 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 832，观测区间 768 - 1984，5 个样本
- 高度 中位数 1216，观测区间 1120 - 1344，5 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 1，观测区间 0.3 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 34，观测区间 20 - 35，5 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 5，5 个样本，取值集中（一致性 90%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，5 个样本，一致性 40%
- 调度器 最常用 karras，5 个样本，一致性 80%
- 重绘幅度 中位数 0.55，观测区间 0.45 - 1，5 个样本
