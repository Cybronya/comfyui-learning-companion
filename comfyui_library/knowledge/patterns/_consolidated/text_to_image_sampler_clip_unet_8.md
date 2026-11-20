---
name: text_to_image_sampler_clip_unet_8
type: Text To Image
frequency: 26
level: weak
coverage: 0.996808
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/10texttoimagefast_2049395761896493057.json, 图片生成/反推提示词/10wutdydiylf_2059686073575497730.json, 图片生成/图生图/Anima base-v11｜10步极速文生图_2079165843375738882.json, 图片生成/图生图/Flux 2 Dev 单图编辑 + 加速版_1994947122980118530.json, 图片生成/图生图/Flux2文生图_1993664157952180226.json, 图片生成/文生图/001.Z-image生图巅峰006.回车批量文生图.json_2033729781623164930.json, 图片生成/文生图/Anima_V10-Turbo 10-Step｜10步极速文生图_2079037824149573634.json, 图片生成/文生图/Anima强大的动漫文生图turbo高速版_2061065103197425666.json, 图片生成/文生图/Boogu_Turbo 文生图_2069444653648273409.json, 图片生成/文生图/Boogu_Turbo_文生图工作流_2069274849616416770.json, 图片生成/文生图/Boogu文生图标准版_2068941708238352385.json, 图片生成/文生图/Krea 2 甜美人像_2082369312555356161.json, 图片生成/文生图/Krea2-turbo文生图3D国漫CG场景_2085325906326937602.json, 图片生成/文生图/Krea2动漫人物写实复古风工作流_2073834007481110529.json, 图片生成/文生图/Krea2图图工作流_2072525906350006273.json, 图片生成/文生图/Krea2图图文生图工作流_2095107374737616898.json, 图片生成/文生图/Krea2文生图工作流_2089571875075747842.json, 图片生成/文生图/LH-DMT版本-2.生图片类-028.Z-image回车批量文生图-NF_2016493232032587777.json, 图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json, 图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json, 图片生成/文生图/Z-image-distall-patch文生图_2002052529569579010.json, 图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json, 图片生成/文生图/（贞贞-小情绪版）Z-Image 文生图V1_2001331257915080706.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（11000步）_1996234333444775938.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（24000步）_1996258756096835586.json, 图片生成/文生图/（贞贞Lora）Z-image文生图V2（4500步）_1994676967016439809.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/反推提示词/10texttoimagefast_2049395761896493057.json、图片生成/反推提示词/10wutdydiylf_2059686073575497730.json、图片生成/图生图/Anima base-v11｜10步极速文生图_2079165843375738882.json、图片生成/图生图/Flux 2 Dev 单图编辑 + 加速版_1994947122980118530.json、图片生成/图生图/Flux2文生图_1993664157952180226.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 21/26 个有
- `LoraLoaderModelOnly` —— 17/26 个有
- `easy promptLine` —— 8/26 个有
- `CR Prompt Text` —— 6/26 个有
- `ImageConcatMulti` —— 3/26 个有
- `LayerUtility: PurgeVRAM` —— 2/26 个有
- `PDRatioSelector` —— 2/26 个有
- `RTXVideoSuperResolution` —— 2/26 个有
- `FluxGuidance` —— 1/26 个有
- `ShellAgentPluginOutputText` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 26 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 26 | 48% |
| 采样算法 | euler | - | 26 | 81% |
| 调度器 | simple | - | 26 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| 宽度 | 1080 | 512 - 1920 | 26 | 68% |
| 高度 | 1148 | 248 - 1920 | 26 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，26 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，26 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，26 个样本，一致性 81%
- 调度器 最常用 simple，26 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1920，26 个样本
- 高度 中位数 1148，观测区间 248 - 1920，26 个样本
- 高发问题（13/26 个样本）：Steps较低可能导致细节不足
