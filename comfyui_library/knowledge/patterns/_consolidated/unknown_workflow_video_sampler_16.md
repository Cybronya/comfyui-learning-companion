---
name: unknown_workflow_video_sampler_16
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.975125
common_nodes: [ColorMatch, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAddFlashVSRInput, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoFlashVSRDecoderLoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode]
problems: []
missing: []
members: [图片生成/文生图/Flash VSR-视频超分辨率_2059197290207862785.json, 平台全量/Flash VSR-视频超分辨率-视频放大-速度快效果好_2010939731055484929.json, 平台全量/Flash VSR-视频超分辨率-视频放大-速度快效果好_2096619101857861633.json, 平台全量/Flash VSR-视频高清放大-速度快效果好_2027334804269699074.json, 平台全量/Flash VSR视频极速高清放大超分辨率_1980092067219148801.json, 平台全量/Flash VSR视频超分辨率（速度快效果好）_1979888482430652418.json, 平台全量/Flash_VSR-视频超分辨率_2063975899703373826.json, 平台全量/视频放大变清晰 Flash VSR-视频超分辨率--速度快效果好_2112511941573959682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_16

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Flash VSR-视频超分辨率_2059197290207862785.json、平台全量/Flash VSR-视频超分辨率-视频放大-速度快效果好_2010939731055484929.json、平台全量/Flash VSR-视频超分辨率-视频放大-速度快效果好_2096619101857861633.json、平台全量/Flash VSR-视频高清放大-速度快效果好_2027334804269699074.json、平台全量/Flash VSR视频极速高清放大超分辨率_1980092067219148801.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `ColorMatch`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAddFlashVSRInput`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoFlashVSRDecoderLoader`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 7/8 个有
- `FlashVSR_SM_KSampler` —— 7/8 个有
- `FlashVSR_SM_Model` —— 7/8 个有
- `Int` —— 7/8 个有
- `WanVideoBlockSwap` —— 7/8 个有
- `Label (rgthree)` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `忽略多组孤海` —— 2/8 个有
- `CustomAddLabel` —— 1/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/8 个有
- `GIMMVFI_interpolate` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.54389e+09 | 1.41137e+08 - 1.93631e+09 | 7 | 58% |
| Prompt 约束强度(CFG) | randomize | - | 7 | 100% |
| 采样算法 | 2 | 2 - 2 | 7 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 7 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.54389e+09，观测区间 1.41137e+08 - 1.93631e+09，7 个样本
- Prompt 约束强度(CFG) 最常用 randomize，7 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，7 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，7 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.93631e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
