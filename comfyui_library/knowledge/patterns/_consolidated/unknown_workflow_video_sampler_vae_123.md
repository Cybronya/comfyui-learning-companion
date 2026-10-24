---
name: unknown_workflow_video_sampler_vae_123
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9512
common_nodes: [JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/VACE 14b +Skyreels V2 T2V文生视频稳定版！_1922867883611930626.json, 视频生成/文生视频/VACE 14b 文生视频（WAN2.1）稳定版_1922872818927812610.json, 视频生成/文生视频/Wan2.1-FusionX文生视频加速工作流_1933749868416389122.json, 视频生成/文生视频/WanVACE+CausVid-9步出视频_1925183972802764801.json, 视频生成/文生视频/【效果炸裂！】wan2.1 Vace 14B 人物长像一致高质量图生视频动画_1925755745747292161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_123

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/VACE 14b +Skyreels V2 T2V文生视频稳定版！_1922867883611930626.json、视频生成/文生视频/VACE 14b 文生视频（WAN2.1）稳定版_1922872818927812610.json、视频生成/文生视频/Wan2.1-FusionX文生视频加速工作流_1933749868416389122.json、视频生成/文生视频/WanVACE+CausVid-9步出视频_1925183972802764801.json、视频生成/文生视频/【效果炸裂！】wan2.1 Vace 14B 人物长像一致高质量图生视频动画_1925755745747292161.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 4/5 个有
- `WanVideoVACEEncode` —— 4/5 个有
- `WanVideoVACEModelSelect` —— 4/5 个有
- `TextInput_` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `ImageRepeat` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `WanVideoEmptyEmbeds` —— 1/5 个有
- `WanVideoVACEStartToEndFrame` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
