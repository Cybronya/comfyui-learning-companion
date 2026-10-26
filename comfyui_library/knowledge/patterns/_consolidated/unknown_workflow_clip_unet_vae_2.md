---
name: unknown_workflow_clip_unet_vae_2
type: Unknown Workflow
frequency: 22
level: weak
coverage: 0.964818
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/002.Qwen编辑之王002.二次采样文生图_2034485126217863170.json, 图片生成/文生图/2030248533244256258.json, 图片生成/文生图/2030259700943560706.json, 图片生成/文生图/2030270553520607233.json, 图片生成/文生图/2030517261940822018.json, 图片生成/文生图/60.tonnie-Magic-Wan-Image文生图_2009063719375998977.json, 图片生成/文生图/Animate动漫出图Qwen工作流_2047157124668592129.json, 图片生成/文生图/Animate动漫出图Qwen工作流_2049757423077957634.json, 图片生成/文生图/Qwen-Image一键生成不知火舞真实版_2042047842927255553.json, 图片生成/文生图/Qwen2512腿精巨长腿背影杀腿部调节_2019638224775290882.json, 图片生成/文生图/Z-I-B道具快乐美女_2040453074061369345.json, 图片生成/文生图/Z-I-B长腿肉腿刺客美女_2056916021260410881.json, 图片生成/文生图/Z-Image-Base文生图亮亮丝袜美女_2018164986979295233.json, 图片生成/文生图/Z-Imgae一键生成大胸美女_2028683377297072130.json, 图片生成/文生图/Z-image一键美女文生图_2023344603134431233.json, 图片生成/文生图/Z-image大码瑜伽裤模特_2054817937000804354.json, 图片生成/文生图/Z-image真实文生图_2027593525369507841.json, 图片生成/文生图/Z-image真实文生图_2096478812799328257.json, 图片生成/文生图/Z-image真实文生图无限制_2021242393848188929.json, 图片生成/文生图/Z-image韩国美少女写真_2040461723756400642.json, 图片生成/文生图/Z-image高中女生校服丝袜写真_2025507598744690689.json, 图片生成/文生图/qwen2512文生图_2058014938349785090.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/002.Qwen编辑之王002.二次采样文生图_2034485126217863170.json、图片生成/文生图/2030248533244256258.json、图片生成/文生图/2030259700943560706.json、图片生成/文生图/2030270553520607233.json、图片生成/文生图/2030517261940822018.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 21/22 个有
- `LoraLoaderModelOnly` —— 21/22 个有
- `CompressImages` —— 17/22 个有
- `PathchSageAttentionKJ` —— 3/22 个有
- `easy promptLine` —— 2/22 个有
- `CheckpointLoaderSimple` —— 1/22 个有
- `KSamplerAdvanced` —— 1/22 个有
- `LatentUpscaleBy` —— 1/22 个有
- `Primitive string multiline [Crystools]` —— 1/22 个有
- `easy promptConcat` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 21 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 22 | 28% |
| 采样算法 | euler | - | 22 | 95% |
| 调度器 | simple | - | 22 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，21 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，22 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，22 个样本，一致性 95%
- 调度器 最常用 simple，22 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 高发问题（18/22 个样本）：Steps较低可能导致细节不足
