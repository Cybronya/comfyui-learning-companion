---
name: unknown_workflow_video_sampler_vae_57
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.995
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX-VACE加速高细节最强首尾帧_1934640445391872001.json, 视频生成/图生视频/FusionX-VACE首尾帧_1934644328725684226.json, 视频生成/图生视频/FusionX高细节双图首尾帧视频生成_1943227565869842433.json, 视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧加速工作流_1935621169481711618.json, 视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json, 视频生成/图生视频/最强模型FusionX加速高细节图生视频_1934634580886659073.json, 视频生成/图生视频/自己用：FusionX双图首尾帧视频生成+lora_1945368931681095682.json, 视频生成/图生视频/🦖FusionX高细节首尾帧_1934430559047217153.json, 视频生成/文生视频/wan2.1-fusionx系列文生视频（加lora版）_1938193111518744578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_57

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/FusionX-VACE加速高细节最强首尾帧_1934640445391872001.json、视频生成/图生视频/FusionX-VACE首尾帧_1934644328725684226.json、视频生成/图生视频/FusionX高细节双图首尾帧视频生成_1943227565869842433.json、视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧加速工作流_1935621169481711618.json、视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 8/9 个有
- `ImageResizeKJ` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `WanVideoVACEStartToEndFrame` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 5/9 个有
- `WanVideoTeaCache` —— 5/9 个有
- `JWInteger` —— 4/9 个有
- `RH_Translator` —— 4/9 个有
- `WanVideoMagCache` —— 4/9 个有
- `easy int` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `WanVideoLoraSelect` —— 3/9 个有
- `Text` —— 2/9 个有
- `ColorMatch` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `WanVideoVACEModelSelect` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
