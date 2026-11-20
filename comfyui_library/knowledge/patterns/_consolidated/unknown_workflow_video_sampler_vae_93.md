---
name: unknown_workflow_video_sampler_vae_93
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.948167
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE 14B OpenPose姿势控制视频转绘工作流_1922746877819895810.json, 平台全量/VACE 14B深度控制视频转绘工作流_1922746842847612929.json, 平台全量/VACE14B-item-swap-v1_1943187729989722114.json, 视频生成/图生视频/VACE 14b 图生视频（支持超长帧数）稳定工作流V2（上次保存错了）_1922692258477522945.json, 视频生成/文生视频/MoviiGen超强动作细节表达高清文生视频优化版V1_1923351101066629121.json, 视频生成/文生视频/VACE 14b +Skyreels V2 T2V文生视频稳定版！_1922867883611930626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_93

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/VACE 14B OpenPose姿势控制视频转绘工作流_1922746877819895810.json、平台全量/VACE 14B深度控制视频转绘工作流_1922746842847612929.json、平台全量/VACE14B-item-swap-v1_1943187729989722114.json、视频生成/图生视频/VACE 14b 图生视频（支持超长帧数）稳定工作流V2（上次保存错了）_1922692258477522945.json、视频生成/文生视频/MoviiGen超强动作细节表达高清文生视频优化版V1_1923351101066629121.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `TextInput_` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `AIO_Preprocessor` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `DepthAnything_V2` —— 1/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/6 个有
- `Image To Mask` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `VHS_VideoInfoSource` —— 1/6 个有
- `WanVideoEmptyEmbeds` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
