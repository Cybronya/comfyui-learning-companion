---
name: unknown_workflow_sampler_vae_40
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.912375
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 -首帧参考生视频-开源版-智能分镜助手-本地可运行_2084117187484282882.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首帧参考生视频_2084114585820422145.json, 视频生成/图生视频/MiniMax H3 单图参考生视频_2084187514818097153.json, 视频生成/图生视频/MiniMax H3 首尾帧参考生视频_2084138245323055105.json, 视频生成/图生视频/MiniMax H3-地图旅游_2085244875817177090.json, 视频生成/图生视频/MiniMax H3-地图旅游_2089683283566223362.json, 视频生成/图生视频/MiniMax H3-现实世界手绘特效_2085245279707688962.json, 视频生成/图生视频/MiniMax H3-现实世界手绘特效_2086663800769572866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_40

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 -首帧参考生视频-开源版-智能分镜助手-本地可运行_2084117187484282882.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-首帧参考生视频_2084114585820422145.json、视频生成/图生视频/MiniMax H3 单图参考生视频_2084187514818097153.json、视频生成/图生视频/MiniMax H3 首尾帧参考生视频_2084138245323055105.json、视频生成/图生视频/MiniMax H3-地图旅游_2085244875817177090.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CreateVideo`
- `LoadImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAFirstFrameCondition`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 5/8 个有
- `llama_cpp_model_loader` —— 5/8 个有
- `llama_cpp_parameters` —— 5/8 个有
- `easy showAnything` —— 4/8 个有
- `ImageResize+` —— 3/8 个有
- `PreviewAny` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `MultiplePathsInput` —— 2/8 个有
- `Qwen3_VQA` —— 2/8 个有
- `VideoLoaderPlus` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
