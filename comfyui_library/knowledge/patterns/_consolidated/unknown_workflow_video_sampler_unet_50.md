---
name: unknown_workflow_video_sampler_unet_50
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.889143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Float to Int, GetVideoComponents, ImageConcatenate_UTK, ImageFromBatch, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, Video Duration Calculator, easy MiniMaxH3ReferenceToVideoBridge, easy imageCount, easy mathInt, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1_2101623619452489730.json, 视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1_2104536932100435969.json, 视频生成/图生视频/开源版MinimaxH3视频编辑去除人物去除物品去除元素_2086518899704680449.json, 视频生成/图生视频/开源版MinimaxH3视频编辑视频参考编辑人物替换人物替换物品替换元素等_2086528754960125953.json, 视频生成/视频生视频/MinimaxH3去水印字幕图标+人物替换V1_2087705335275540481.json, 视频生成/视频生视频/MinimaxH3视频参考编辑人物替换T1_2086361427148886017.json, 视频生成/视频生视频/MinimaxH3视频编辑V1去除背景中的人物_2085963862112817154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1_2101623619452489730.json、视频生成/图生视频/MinimaxH3视频参考编辑人物替换T1_2104536932100435969.json、视频生成/图生视频/开源版MinimaxH3视频编辑去除人物去除物品去除元素_2086518899704680449.json、视频生成/图生视频/开源版MinimaxH3视频编辑视频参考编辑人物替换人物替换物品替换元素等_2086528754960125953.json、视频生成/视频生视频/MinimaxH3去水印字幕图标+人物替换V1_2087705335275540481.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `Video Duration Calculator`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `easy imageCount`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ExtractStoryboards_xuhuan1024` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `InspyrenetRembg` —— 4/7 个有
- `easy indexAnything` —— 4/7 个有
- `CR Image Grid Panel` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `FlashVSR_SM_KSampler` —— 1/7 个有
- `FlashVSR_SM_Model` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.24096e+08 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 4.24096e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
