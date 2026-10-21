---
name: text_to_image_lora_sampler_clip_119
type: Text To Image
frequency: 9
level: strong
coverage: 0.868
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json, 图片生成/文生图/gemini3.6文生图AI绘画生成工作流_2088403565512585218.json, 图片生成/文生图/gemini3.6视频6图双文本生成｜多模态文生图工作流_2096731827070390274.json, 图片生成/文生图/mini图生视频一键生成｜Seedance2.0图片转视频_2095874894868336642.json, 图片生成/文生图/小空间可加视频｜gemini3.6文生图轻量玩法_2089033642176770049.json, 图片生成/文生图/文生图图片生成｜gemini3.6工作流_2088382298440953858.json, 视频生成/图生视频/Seedance2.0 Mini多模态｜文生图生视频全都能跑_2106629854375534594.json, 视频生成/图生视频/Seedance_2.5多模态全能参考视频｜图生视频视频生视频双支持_2101899070481719297.json, 视频生成/文生视频/宽审多图多视频参考｜pipi-Seedance2.0-global生成_2095579714701316098.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Seedance2.0 mini图生视频｜图片秒变高质量视频_2106631464661114881.json、图片生成/文生图/gemini3.6文生图AI绘画生成工作流_2088403565512585218.json、图片生成/文生图/gemini3.6视频6图双文本生成｜多模态文生图工作流_2096731827070390274.json、图片生成/文生图/mini图生视频一键生成｜Seedance2.0图片转视频_2095874894868336642.json、图片生成/文生图/小空间可加视频｜gemini3.6文生图轻量玩法_2089033642176770049.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `PreviewAny` —— 4/9 个有
- `RHLLMChatNode` —— 4/9 个有
- `easy saveText` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `LoadAudio` —— 2/9 个有
- `MuyeTextEditOutput` —— 2/9 个有
- `RH_RhartVideoSparkvideo20MiniImageToVideo` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `RH_BytedanceSeedance20GlobalMultimodalVideo` —— 1/9 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 1/9 个有
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
