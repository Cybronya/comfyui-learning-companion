---
name: unknown_workflow_video_sampler_vae_53
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.866778
common_nodes: [INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan图生视频_首尾帧_1931534344593321986.json, 视频生成/图生视频/accvid+vace首尾帧工作流_1928120240486662145.json, 视频生成/图生视频/selfforcing+vace14b lora 版_1938291907363540993.json, 视频生成/图生视频/selfforcing+vace首尾帧（5连拍生成视频）_1939027395783675906.json, 视频生成/图生视频/vace+movii-gen图生视频_1924712170221654017.json, 视频生成/图生视频/vace+movii-gen图生视频增强引导_1924723933575376897.json, 视频生成/图生视频/vace+moviigen+causvid图生视频_1924709623990054913.json, 视频生成/图生视频/vace_多主体引用_1923283669073448961.json, 视频生成/图生视频/vace_首帧尾帧_1923030550234189825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_53

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan图生视频_首尾帧_1931534344593321986.json、视频生成/图生视频/accvid+vace首尾帧工作流_1928120240486662145.json、视频生成/图生视频/selfforcing+vace14b lora 版_1938291907363540993.json、视频生成/图生视频/selfforcing+vace首尾帧（5连拍生成视频）_1939027395783675906.json、视频生成/图生视频/vace+movii-gen图生视频_1924712170221654017.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 8/9 个有
- `WanVideoExperimentalArgs` —— 8/9 个有
- `WanVideoSLG` —— 8/9 个有
- `GetNode` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `WanVideoTorchCompileSettings` —— 6/9 个有
- `WanVideoLoraSelect` —— 5/9 个有
- `WanVideoVACEStartToEndFrame` —— 5/9 个有
- `ImpactMakeImageBatch` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `WanVideoEnhanceAVideo` —— 4/9 个有
- `AutoCropFaces` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `WanVideoTeaCache` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `RMBG` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
