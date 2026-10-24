---
name: text_to_image_lora_sampler_clip_224
type: Text To Image
frequency: 8
level: strong
coverage: 0.83725
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Minimax人物替换｜动作迁移视频处理生成_2094865846144421890.json, 图片生成/图生图/人物替换处理｜Minimax动作迁移视频一键生成_2095056732870496257.json, 数字人/数字人/MinimaxH3 角色替换｜视频换脸动作迁移数字人一键搞定_2096845137870671874.json, 数字人/数字人/MinimaxH3角色替换工作流｜数字人换脸动作迁移生成_2096647400864706561.json, 视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json, 视频生成/图生视频/MiniMax h3开源加速版 海螺多参文生视频图生视频音频参考_2085303974785273857.json, 视频生成/图生视频/MiniMaxH3参考生视频量化加速｜文本图像音频视频全能_2089438111041409026.json, 视频生成/图生视频/minimax h3最强动作迁移｜视频图生视频直出_2092048558504628226.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_224

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Minimax人物替换｜动作迁移视频处理生成_2094865846144421890.json、图片生成/图生图/人物替换处理｜Minimax动作迁移视频一键生成_2095056732870496257.json、数字人/数字人/MinimaxH3 角色替换｜视频换脸动作迁移数字人一键搞定_2096845137870671874.json、数字人/数字人/MinimaxH3角色替换工作流｜数字人换脸动作迁移生成_2096647400864706561.json、视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `ModelAttentionBackend` —— 7/8 个有
- `VHS_LoadVideo` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `VAEDecodeAudio` —— 6/8 个有
- `ImageResizeKJv2` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `ComfyMathExpression` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `GetNode` —— 4/8 个有
- `PrimitiveFloat` —— 4/8 个有
- `ResolutionSelector` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `VHS_VideoInfo` —— 4/8 个有
- `CreateVideo` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `Int` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `SolAttnMiniMax` —— 2/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/8 个有
- `VideoCombineV2` —— 2/8 个有
- `easy int` —— 2/8 个有
- `ComfyMiniMaxH3Director` —— 1/8 个有
- `MiniMaxH3AddGuide` —— 1/8 个有
- `MiniMaxH3BlockCacheT8` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有
- `UniBlockSwapTE` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
