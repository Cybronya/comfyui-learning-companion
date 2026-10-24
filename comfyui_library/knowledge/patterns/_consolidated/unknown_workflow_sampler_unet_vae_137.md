---
name: unknown_workflow_sampler_unet_vae_137
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.741429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json, comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json, comfyui-workflow-templates-json/video_minimax_h3_r2v.json, 视频生成/图生视频/4步MiniMax-H3参考图生视频-LynnReal-Omni_2099804283427446785.json, 视频生成/图生视频/LynnReal-FastH3 pose2v动作迁移_2101573571259752450.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-动作迁移-生成视频-工作流_2093578653677481986.json, 视频生成/图生视频/MinimaxH3人物替换character swap_2109965862622031874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_137

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/video_minimax_h3_fun_controlnet_union.json、comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json、comfyui-workflow-templates-json/video_minimax_h3_r2v.json、视频生成/图生视频/4步MiniMax-H3参考图生视频-LynnReal-Omni_2099804283427446785.json、视频生成/图生视频/LynnReal-FastH3 pose2v动作迁移_2101573571259752450.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `LoadVideo` —— 4/7 个有
- `GetVideoComponents` —— 3/7 个有
- `AnySwitch` —— 2/7 个有
- `Fast Bypasser (rgthree)` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `Video Slice` —— 2/7 个有
- `622cceeb-7ba3-4dd9-b0e8-00066c5222a4` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `LynnRealAlignedReference` —— 1/7 个有
- `MiniMaxH3AddGuide` —— 1/7 个有
- `MiniMaxH3FunControlNetApply` —— 1/7 个有
- `ModelPatchLoader` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `QwenH3PromptLocal` —— 1/7 个有
- `VideoFrameSample` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
