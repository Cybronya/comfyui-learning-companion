---
name: unknown_workflow_video_sampler_unet_18
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.89445
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Float to Int, GetVideoComponents, ImageConcatenate_UTK, ImageFromBatch, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, Video Duration Calculator, easy MiniMaxH3ReferenceToVideoBridge, easy imageCount, easy showAnything]
problems: []
missing: []
members: [平台全量/Minimax3全参模式角色替换_2088453261673189377.json, 平台全量/MinimaxH3视频参考编辑人物换装_2086379854819315713.json, 平台全量/MinimaxH3视频参考编辑人物替换T1_2100058196126818305.json, 平台全量/MinimaxH3视频参考编辑人物替换T1_2100138545330606082.json, 平台全量/MinimaxH3视频编辑V1去除噪点图像高清_2087011033864040449.json, 平台全量/MinimaxH3视频编辑V2去除噪点图像高清_2087058836132814849.json, 平台全量/MinimaxH3视频编辑去除人物2_2086405322138275841.json, 平台全量/MinimaxH3视频编辑去除人物_2086394740144164865.json, 平台全量/MinimaxH3视频编辑去除人物_2100404980300738561.json, 平台全量/MinimaxH3视频编辑去除人物_2100493540882210818.json, 平台全量/minimaxH3视频编辑复刻抖音热门特效V1_2087938018350034946.json, 平台全量/开源版Minimax H3 视频编辑去除人物去除物品去除元素_2086767381459857409.json, 数字人/数字人/MinimaxH3视频参考换人_2115081882764402689.json, 视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1_2101623619452489730.json, 视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1_2104536932100435969.json, 视频生成/图生视频/开源版MinimaxH3视频编辑去除人物去除物品去除元素_2086518899704680449.json, 视频生成/图生视频/开源版MinimaxH3视频编辑视频参考编辑人物替换人物替换物品替换元素等_2086528754960125953.json, 视频生成/视频生视频/MinimaxH3去水印字幕图标+人物替换V1_2087705335275540481.json, 视频生成/视频生视频/MinimaxH3视频参考编辑人物替换T1_2086361427148886017.json, 视频生成/视频生视频/MinimaxH3视频编辑V1去除背景中的人物_2085963862112817154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_18

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（平台全量/Minimax3全参模式角色替换_2088453261673189377.json、平台全量/MinimaxH3视频参考编辑人物换装_2086379854819315713.json、平台全量/MinimaxH3视频参考编辑人物替换T1_2100058196126818305.json、平台全量/MinimaxH3视频参考编辑人物替换T1_2100138545330606082.json、平台全量/MinimaxH3视频编辑V1去除噪点图像高清_2087011033864040449.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Float to Int`
- `GetVideoComponents`
- `ImageConcatenate_UTK`
- `ImageFromBatch`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `Video Duration Calculator`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy mathInt` —— 19/20 个有
- `Text` —— 18/20 个有
- `ExtractStoryboards_xuhuan1024` —— 17/20 个有
- `PreviewImage` —— 17/20 个有
- `LoadImage` —— 13/20 个有
- `easy indexAnything` —— 10/20 个有
- `CR Image Grid Panel` —— 9/20 个有
- `InspyrenetRembg` —— 7/20 个有
- `LoraLoaderModelOnly` —— 4/20 个有
- `FlashVSR_SM_KSampler` —— 3/20 个有
- `FlashVSR_SM_Model` —— 3/20 个有
- `JWInteger` —— 3/20 个有
- `LayerUtility: PurgeVRAM V2` —— 3/20 个有
- `EmptyImage` —— 1/20 个有
- `PathchSageAttentionKJ` —— 1/20 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/20 个有
- `easy mathFloat` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.27907e+09 | 4.24096e+08 - 1.74736e+09 | 3 | 52% |
| Prompt 约束强度(CFG) | randomize | - | 3 | 100% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.27907e+09，观测区间 4.24096e+08 - 1.74736e+09，3 个样本
- Prompt 约束强度(CFG) 最常用 randomize，3 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.74736e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
