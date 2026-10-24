---
name: unknown_workflow_sampler_unet_vae_38
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.947375
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/视频编辑，视频创作 LTX导演台V2_2069660528036892673.json, 视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json, 视频生成/文生视频/LTX Director （导演节点）多功能 视频生成工作流_2056619920078753794.json, 视频生成/文生视频/LTX2.3 Director 导演工作台_2057724826655219714.json, 视频生成/文生视频/LTX2.3-Director 导演台-多图漫剧长视频_2062370729332662273.json, 视频生成/文生视频/LTX2.3-Director 导演台-多图短剧漫剧长视频_2063220192473341953.json, 视频生成/文生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-文生视频_2075921500900782081.json, 视频生成/文生视频/LTX2.3导演台V2+图生视频工作流_2072015806417956866.json, 视频生成/文生视频/LTX2.3导演台V2.0_2077936049308917761.json, 视频生成/文生视频/LTX2.3导演台_原生音视频_修复版_2073961723706560514.json, 视频生成/文生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2075912339274162178.json, 视频生成/文生视频/LTX_Director_2_Workflow_FL_frame1_2072131735323758594.json, 视频生成/文生视频/LTX_Director_2_Workflow_extend_video_2070694601605861377.json, 视频生成/文生视频/LTX_Director_2_Workflow_iclora_edit_video_2070699701174890498.json, 视频生成/文生视频/LTX_Director_2_Workflow_retake_mode_2070703453340524545.json, 视频生成/文生视频/【3D白模转真实】LTX-2.3 真实物理渲染与驱动_2073385860002832386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_38

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/视频编辑，视频创作 LTX导演台V2_2069660528036892673.json、视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json、视频生成/文生视频/LTX Director （导演节点）多功能 视频生成工作流_2056619920078753794.json、视频生成/文生视频/LTX2.3 Director 导演工作台_2057724826655219714.json、视频生成/文生视频/LTX2.3-Director 导演台-多图漫剧长视频_2062370729332662273.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `LTXVConditioning` —— 15/16 个有
- `LTXVLatentUpsampler` —— 15/16 个有
- `LatentUpscaleModelLoader` —— 15/16 个有
- `CreateVideo` —— 14/16 个有
- `SaveVideo` —— 14/16 个有
- `LTXDirectorCropGuides` —— 12/16 个有
- `ModelPreviewOverrideKJ` —— 12/16 个有
- `VAELoader` —— 11/16 个有
- `LoraLoaderModelOnly` —— 6/16 个有
- `LTX2SamplingPreviewOverride` —— 4/16 个有
- `LTXVCropGuides` —— 4/16 个有
- `CLIPTextEncode` —— 2/16 个有
- `GetNode` —— 2/16 个有
- `SetNode` —— 2/16 个有
- `VHS_VideoCombine` —— 2/16 个有
- `LTX2_NAG` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有
- `Mesh2MotionExplore` —— 1/16 个有
- `Power Lora Loader (rgthree)` —— 1/16 个有
- `Text` —— 1/16 个有
- `Text Multiline` —— 1/16 个有
- `孤海注释` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
