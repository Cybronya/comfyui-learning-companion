---
name: unknown_workflow_video_lora_sampler_426
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.923
common_nodes: [DrawGaussianNoiseOnImage, DrawMaskOnImage, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJv2, InvertMask, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUniLumosEmbeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/UniLumosRelight视频重打光_重上色工作流_1987987738475565058.json, 平台全量/UniLumos一键换视频背景+自动打光_1990230693739417602.json, 平台全量/UniLumos一键换视频背景+重新打光_1989204009275756546.json, 平台全量/Unilumos+FlashVSR超分视频重打光V1_1988176085563170817.json, 平台全量/Unilumos视频重打光V1_1988141417442754561.json, 平台全量/Unilumos视频重打光_2073263081320435713.json, 视频生成/图生视频/Unilumos+单图背景人物融合+FlashVSR超分视频重打光V1_1988230649322586114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_426

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/UniLumosRelight视频重打光_重上色工作流_1987987738475565058.json、平台全量/UniLumos一键换视频背景+自动打光_1990230693739417602.json、平台全量/UniLumos一键换视频背景+重新打光_1989204009275756546.json、平台全量/Unilumos+FlashVSR超分视频重打光V1_1988176085563170817.json、平台全量/Unilumos视频重打光V1_1988141417442754561.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `DrawGaussianNoiseOnImage`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `InvertMask`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoUniLumosEmbeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageRemoveBackground+` —— 6/7 个有
- `TransparentBGSession+` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `WanVideoTorchCompileSettings` —— 4/7 个有
- `JWInteger` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `FlashVSR_SM_KSampler` —— 2/7 个有
- `FlashVSR_SM_Model` —— 2/7 个有
- `ImpactInt` —— 2/7 个有
- `PDIMAGE_LongerSize` —— 2/7 个有
- `RepeatImageBatch` —— 2/7 个有
- `VHS_VideoInfo` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `ImageRepeat` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `VHS_VideoInfoSource` —— 1/7 个有
- `easy imageRemBg` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.17799e+09 | - | 2 | 27% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.17799e+09，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.04285e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
