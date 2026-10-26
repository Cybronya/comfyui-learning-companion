---
name: unknown_workflow_upscale_latent_upscale_sampler_9
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.899364
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3导演台V2.0_2077936049308917761.json, 视频生成/文生视频/LTX2.3导演台_原生音视频_修复版_2073961723706560514.json, 视频生成/文生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2075912339274162178.json, 视频生成/文生视频/LTX_Director_2_Workflow_FL_frame1_2072131735323758594.json, 视频生成/文生视频/LTX_Director_2_Workflow_extend_video_2070694601605861377.json, 视频生成/文生视频/LTX_Director_2_Workflow_iclora_edit_video_2070699701174890498.json, 视频生成/文生视频/LTX_Director_2_Workflow_retake_mode_2070703453340524545.json, 视频生成/文生视频/LTX导演台2.0【Director】优化工作流已修复_2060326139540885505.json, 视频生成/文生视频/LTX导演台2.0【Director】视频延长+编辑_2069229270215516161.json, 视频生成/文生视频/【3D白模转真实】LTX-2.3 真实物理渲染与驱动_2073385860002832386.json, 视频生成/文生视频/工作流基础系列29-LTX 2.3+Director导演台_2064315632790892545.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/LTX2.3导演台V2.0_2077936049308917761.json、视频生成/文生视频/LTX2.3导演台_原生音视频_修复版_2073961723706560514.json、视频生成/文生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2075912339274162178.json、视频生成/文生视频/LTX_Director_2_Workflow_FL_frame1_2072131735323758594.json、视频生成/文生视频/LTX_Director_2_Workflow_extend_video_2070694601605861377.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXDirectorCropGuides` —— 10/11 个有
- `LTXVConditioning` —— 10/11 个有
- `ModelPreviewOverrideKJ` —— 10/11 个有
- `ConditioningZeroOut` —— 9/11 个有
- `VAELoader` —— 9/11 个有
- `CreateVideo` —— 7/11 个有
- `SaveVideo` —— 7/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `CLIPTextEncode` —— 5/11 个有
- `LTX2_NAG` —— 4/11 个有
- `VHS_VideoCombine` —— 4/11 个有
- `LoadImage` —— 3/11 个有
- `GetNode` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `LTXVCropGuides` —— 1/11 个有
- `Mesh2MotionExplore` —— 1/11 个有
- `Power Lora Loader (rgthree)` —— 1/11 个有
- `PreviewAudio` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
