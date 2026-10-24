---
name: text_to_image_lora_sampler_clip_357
type: Text To Image
frequency: 5
level: strong
coverage: 0.803
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物参考跳舞生成 海螺H3标准工作流视频运镜_2094248116324233218.json, 图片生成/图生图/全能参考视频Minimax H3 V2工作流，图生图多参考视频生成方案_2107989147045683201.json, 图片生成/图生图/电商产品替换流｜场景中加人物商品图秒变带货大片_2112898782546452481.json, 图片生成/图生图/首尾帧生视频 海螺H3标准工作流图生图生视频_2094245287912099842.json, 视频生成/图生视频/海螺H3人物替换｜动作迁移角色一致性生成_2095271195703857153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_357

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人物参考跳舞生成 海螺H3标准工作流视频运镜_2094248116324233218.json、图片生成/图生图/全能参考视频Minimax H3 V2工作流，图生图多参考视频生成方案_2107989147045683201.json、图片生成/图生图/电商产品替换流｜场景中加人物商品图秒变带货大片_2112898782546452481.json、图片生成/图生图/首尾帧生视频 海螺H3标准工作流图生图生视频_2094245287912099842.json、视频生成/图生视频/海螺H3人物替换｜动作迁移角色一致性生成_2095271195703857153.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `MiniMaxH3SigmaShift` —— 4/5 个有
- `ModelAttentionBackend` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `VAEDecodeAudio` —— 4/5 个有
- `easy anythingIndexSwitch` —— 4/5 个有
- `easy int` —— 4/5 个有
- `ComfyMathExpression` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `Bookmark (rgthree)` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/5 个有
- `PlaySound|pysssss` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `ImageUpscaleWithModelBatched` —— 1/5 个有
- `MiniMaxH3ImageToVideo` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
