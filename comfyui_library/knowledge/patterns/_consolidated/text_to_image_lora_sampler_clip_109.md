---
name: text_to_image_lora_sampler_clip_109
type: Text To Image
frequency: 13
level: strong
coverage: 0.705154
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物参考跳舞生成 海螺H3标准工作流视频运镜_2094248116324233218.json, 图片生成/图生图/全能参考视频Minimax H3 V2工作流，图生图多参考视频生成方案_2107989147045683201.json, 图片生成/图生图/故事多分镜图处理｜Minimax h3高一致性出图_2093805215270129666.json, 图片生成/图生图/故事多分镜高一致性｜Minimax h3场景环境图处理_2094026676677210113.json, 图片生成/图生图/电商产品替换流｜场景中加人物商品图秒变带货大片_2112898782546452481.json, 图片生成/图生图/电商产品替换视频版｜商品展示加视频超分画质一步到顶_2112923090907910145.json, 图片生成/图生图/首尾帧生视频 海螺H3标准工作流图生图生视频_2094245287912099842.json, 图片生成/文生图/MINIMAX H3全功能加速短剧神器工作流，文生图图生图高效创作方案_2106896826518560769.json, 图片生成/文生图/MINIMax H3短剧神器｜全功能加速文生图图生图_2106595105699360770.json, 视频生成/图生视频/MINIMAX_H3全功能加速短剧神器工作流，文生图图生图高效创作方案_2108736968589926402.json, 视频生成/文生视频/H3全功能多重加速V2短剧神器 视频生成处理工具_2100689948386091009.json, 视频生成/文生视频/海螺H3全功能多重加速V2短剧神器｜minimax h3文生视频图生视频数字人通吃_2100444550102872066.json, 视频生成/文生视频/海螺H3全功能文生视频工作流h3多重加速V2短剧神器minimax_2087334573154856962.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/人物参考跳舞生成 海螺H3标准工作流视频运镜_2094248116324233218.json、图片生成/图生图/全能参考视频Minimax H3 V2工作流，图生图多参考视频生成方案_2107989147045683201.json、图片生成/图生图/故事多分镜图处理｜Minimax h3高一致性出图_2093805215270129666.json、图片生成/图生图/故事多分镜高一致性｜Minimax h3场景环境图处理_2094026676677210113.json、图片生成/图生图/电商产品替换流｜场景中加人物商品图秒变带货大片_2112898782546452481.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 13 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 12/13 个有
- `VAEDecodeAudio` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `ComfyMathExpression` —— 11/13 个有
- `PrimitiveFloat` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `ResolutionSelector` —— 10/13 个有
- `easy int` —— 10/13 个有
- `ModelAttentionBackend` —— 9/13 个有
- `VHS_LoadVideo` —— 9/13 个有
- `Bookmark (rgthree)` —— 8/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `GetNode` —— 8/13 个有
- `PlaySound|pysssss` —— 8/13 个有
- `SetNode` —— 8/13 个有
- `MiniMaxH3ImageToVideo` —— 7/13 个有
- `SaveImage` —— 7/13 个有
- `Any Switch (rgthree)` —— 6/13 个有
- `Fast Groups Muter (rgthree)` —— 6/13 个有
- `LoadAudio` —— 6/13 个有
- `Mute / Bypass Relay (rgthree)` —— 6/13 个有
- `Mute / Bypass Repeater (rgthree)` —— 6/13 个有
- `SetReserveVRAM` —— 6/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/13 个有
- `GetImageSizeAndCount` —— 4/13 个有
- `ImageResizeKJv2` —— 4/13 个有
- `MiniMaxH3SigmaShift` —— 4/13 个有
- `PrimitiveInt` —— 4/13 个有
- `VHS_VideoCombine` —— 4/13 个有
- `easy anythingIndexSwitch` —— 4/13 个有
- `BlockSparseAttention` —— 3/13 个有
- `EasyCache` —— 3/13 个有
- `ManualSigmas` —— 3/13 个有
- `GetImagesFromBatchIndexed` —— 2/13 个有
- `GetVideoComponents` —— 2/13 个有
- `VHS_VideoInfo` —— 2/13 个有
- `EmptyImage` —— 1/13 个有
- `ImageUpscaleWithModelBatched` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `RIFE VFI` —— 1/13 个有
- `TrimAudioDuration` —— 1/13 个有
- `UpscaleModelLoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
