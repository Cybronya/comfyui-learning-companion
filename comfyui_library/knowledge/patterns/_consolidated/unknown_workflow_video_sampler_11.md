---
name: unknown_workflow_video_sampler_11
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8584
common_nodes: [DiffuEraserLoader, DiffuEraserSampler, ImageConcanate, ImageFromBatch+, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, RepeatImageBatch, SaveImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/4.19号版本豆包（9_16竖版）seedance2.0水印去除+高清化V3_2045782308111785985.json, 图片生成/图生图/全能视频S横版视频动态水印消除V5（支持音频）_1974464932060205057.json, 视频生成/图生视频/4.19横版16_9豆包官方版seedance2.0水印去除+高清化V3_2045784226385104897.json, 视频生成/图生视频/Ltx2.3字幕乱码去除+高清化V3（需要自己调整蒙版）_2043949321623707650.json, 视频生成/图生视频/即梦官方版seedance2.0水印去除+高清化V2（9_16竖版）_2020315533945606146.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_11

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/4.19号版本豆包（9_16竖版）seedance2.0水印去除+高清化V3_2045782308111785985.json、图片生成/图生图/全能视频S横版视频动态水印消除V5（支持音频）_1974464932060205057.json、视频生成/图生视频/4.19横版16_9豆包官方版seedance2.0水印去除+高清化V3_2045784226385104897.json、视频生成/图生视频/Ltx2.3字幕乱码去除+高清化V3（需要自己调整蒙版）_2043949321623707650.json、视频生成/图生视频/即梦官方版seedance2.0水印去除+高清化V2（9_16竖版）_2020315533945606146.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `RepeatImageBatch`
- `SaveImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `FlashVSR_SM_KSampler` —— 4/5 个有
- `FlashVSR_SM_Model` —— 4/5 个有
- `GetVideoComponents` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `SaveVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.33535e+09 | 7.59123e+08 - 1.84687e+09 | 4 | 63% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 100% |
| 采样算法 | 2 | 2 - 2 | 4 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.33535e+09，观测区间 7.59123e+08 - 1.84687e+09，4 个样本
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.84687e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
