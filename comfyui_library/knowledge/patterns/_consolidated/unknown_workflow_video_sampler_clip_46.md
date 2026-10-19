---
name: unknown_workflow_video_sampler_clip_46
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.493091
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2006247037502758914.json, 视频生成/图生视频/1999107369680371713.json, 视频生成/图生视频/2000487723846729730.json, 视频生成/图生视频/2006292810990882817.json, 视频生成/图生视频/2016050718058221570.json, 视频生成/图生视频/2013893086845341698.json, 视频生成/图生视频/2055902519104163842.json, 视频生成/图生视频/1986333709685194753.json, 视频生成/图生视频/2003771509095211009.json, 视频生成/图生视频/1999623009306636290.json, 视频生成/图生视频/1988509206477234177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2006247037502758914.json、视频生成/图生视频/1999107369680371713.json、视频生成/图生视频/2000487723846729730.json、视频生成/图生视频/2006292810990882817.json、视频生成/图生视频/2016050718058221570.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Int` —— 10/11 个有
- `WanImageToVideo` —— 10/11 个有
- `wanBlockSwap` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `PreviewImage` —— 6/11 个有
- `RIFE VFI` —— 6/11 个有
- `ImageResizeKJv2` —— 5/11 个有
- `PrimitiveStringMultiline` —— 5/11 个有
- `WanFirstLastFrameToVideo` —— 5/11 个有
- `easy int` —— 5/11 个有
- `ImageLoader` —— 3/11 个有
- `CR Text` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `ImpactInt` —— 1/11 个有
- `PainterI2V` —— 1/11 个有
- `easy promptReplace` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 82% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 11 | 100% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | normal | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 82%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 normal，11 个样本，一致性 100%
