---
name: unknown_workflow_video_lora_sampler_405
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.901
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AniWan专业动漫模型版图生视频_1945026256120504322.json, 视频生成/图生视频/AniWan专业动漫模型版图生视频lightx2v发布_1947494029451743234.json, 视频生成/图生视频/AniWan专业动漫模型版图生视频lightx2v对比_1945320881478410242.json, 视频生成/图生视频/FastWan图生视频_1949619051676475394.json, 视频生成/图生视频/Radial 提速20% wan2.1图生视频工作流_1947317723317555201.json, 视频生成/图生视频/Radial 提速20% 万相图生视频工作流_1946283928597458945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_405

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/AniWan专业动漫模型版图生视频_1945026256120504322.json、视频生成/图生视频/AniWan专业动漫模型版图生视频lightx2v发布_1947494029451743234.json、视频生成/图生视频/AniWan专业动漫模型版图生视频lightx2v对比_1945320881478410242.json、视频生成/图生视频/FastWan图生视频_1949619051676475394.json、视频生成/图生视频/Radial 提速20% wan2.1图生视频工作流_1947317723317555201.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 3/6 个有
- `WanVideoSetRadialAttention` —— 2/6 个有
- `CR Upscale Image` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `ShellAgentPluginInputImage` —— 1/6 个有
- `ShellAgentPluginInputText` —— 1/6 个有
- `ShellAgentPluginSaveVideoVHS` —— 1/6 个有
- `WanVideoEasyCache` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
