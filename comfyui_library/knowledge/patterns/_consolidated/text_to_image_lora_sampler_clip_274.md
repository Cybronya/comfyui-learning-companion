---
name: text_to_image_lora_sampler_clip_274
type: Text To Image
frequency: 7
level: strong
coverage: 0.904714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/剧情生成天花板｜故事板一键产出SD2绘图声纹参考全套_2089839351608991746.json, 数字人/数字人/HeyGem视频换声工作流｜语音迁移保留原画面_2106623816477794305.json, 数字人/数字人/HeyGem语音迁移换声｜视频配音一键替换原声_2097222877983625217.json, 数字人/数字人/Heygem真人对口型数字人｜口播长视频快速生成书评国学情感_2110692840987783169.json, 数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json, 视频生成/图生视频/真人对口型口播｜Heygem书评国学情感数字人超长视频_2091209074963730434.json, 音频生成/音频生成/Heygem数字人带货对口型｜IndexTTS文字生成音频工作流_2097050749023903746.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_274

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/剧情生成天花板｜故事板一键产出SD2绘图声纹参考全套_2089839351608991746.json、数字人/数字人/HeyGem视频换声工作流｜语音迁移保留原画面_2106623816477794305.json、数字人/数字人/HeyGem语音迁移换声｜视频配音一键替换原声_2097222877983625217.json、数字人/数字人/Heygem真人对口型数字人｜口播长视频快速生成书评国学情感_2110692840987783169.json、数字人/数字人/数字人口播形象视频｜口播带货数字人批量做_2097215283814559746.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_HeyGemNode` —— 5/7 个有
- `LoadVideo` —— 3/7 个有
- `AudioCrop` —— 2/7 个有
- `CR Prompt Text` —— 2/7 个有
- `CreateVideo` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `IndexTTSRun` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `RH_KlingV2AiAvatarStandardImageAudioToVideo` —— 1/7 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
