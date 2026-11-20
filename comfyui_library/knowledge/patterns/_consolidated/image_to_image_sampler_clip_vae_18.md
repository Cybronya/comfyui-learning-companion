---
name: image_to_image_sampler_clip_vae_18
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9168
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/图生图训练模板_2042065010142224385.json, 图片生成/图生图/工作流基础篇-3-基础图生图工作流（写实和动漫双风格）_2012422631575785474.json, 图片生成/图生图/接力帧净化_SD图生图_3050低显存_2061824613121880066.json, 图片生成/图生图/洗图去AI感_2050522040632913922.json, 图片生成/图生图/清透水润写实图生图+LORA_1982124639554019330.json, 图片生成/图生图/自动化妆2_Automatic makeup2_img2img_1911604879872225281.json, 图片生成/图生图/自动化妆_细节增强器_1896904379117772802.json, 图片生成/图生图/高清画质特写_2049892403997364226.json, 图片生成/图生图/麦橘写实图生图基础版-shure_1982102747661123585.json, 视频生成/文生视频/国风女孩_2055307573456326657.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_18

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图生图训练模板_2042065010142224385.json、图片生成/图生图/工作流基础篇-3-基础图生图工作流（写实和动漫双风格）_2012422631575785474.json、图片生成/图生图/接力帧净化_SD图生图_3050低显存_2061824613121880066.json、图片生成/图生图/洗图去AI感_2050522040632913922.json、图片生成/图生图/清透水润写实图生图+LORA_1982124639554019330.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 9/10 个有
- `LoraLoader` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `ConditioningAverage` —— 2/10 个有
- `RepeatLatentBatch` —— 2/10 个有
- `CheckpointLoaderSimple_Any` —— 1/10 个有
- `Image Compare (mtb)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 10 | 91% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 10 | 96% |
| 采样算法 | dpmpp_2m | - | 10 | 50% |
| 调度器 | karras | - | 10 | 60% |
| 重绘幅度 | 0.515 | 0.22 - 1 | 10 | 50% |
| LoRA 模型强度 | 0.25 | 0 - 1 | 5 | 15% |
| LoRA 文本强度 | 0.54 | 0.27 - 1 | 5 | 58% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，10 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，10 个样本，取值集中（一致性 96%）
- 采样算法 最常用 dpmpp_2m，10 个样本，一致性 50%
- 调度器 最常用 karras，10 个样本，一致性 60%
- 重绘幅度 中位数 0.515，观测区间 0.22 - 1，10 个样本
- LoRA 模型强度 中位数 0.25，观测区间 0 - 1，5 个样本，取值分散，一致性仅 15%
- LoRA 文本强度 中位数 0.54，观测区间 0.27 - 1，5 个样本
