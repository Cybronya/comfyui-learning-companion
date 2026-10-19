---
name: unknown_workflow_lora_sampler_unet_31
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9182
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3爆图工作流，参考图（一次15图）_2093213612537110530.json, 视频生成/图生视频/MiniMaxH3爆图工作流，文生图像（一次15图）_2092562660834496514.json, 视频生成/图生视频/MiniMaxH3爆图工作流，文生图像（一次45图）_2093285352231497729.json, 视频生成/图生视频/MinimaxH3 女友ASMR_2091175012479881217.json, 视频生成/图生视频/MinimaxH3 数字人（文字版）_2084533534718517250.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3爆图工作流，参考图（一次15图）_2093213612537110530.json、视频生成/图生视频/MiniMaxH3爆图工作流，文生图像（一次15图）_2092562660834496514.json、视频生成/图生视频/MiniMaxH3爆图工作流，文生图像（一次45图）_2093285352231497729.json、视频生成/图生视频/MinimaxH3 女友ASMR_2091175012479881217.json、视频生成/图生视频/MinimaxH3 数字人（文字版）_2084533534718517250.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `ExtractStoryboards_xuhuan1024` —— 3/5 个有
- `LTXVConcatAVLatent` —— 3/5 个有
- `LTXVSeparateAVLatent` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `MinimaxH3LatentUpscaler3D` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `SplitSigmas` —— 3/5 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `CharacterCount` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `MiniMaxH3ImageToVideo` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `VAEDecodeAudio` —— 2/5 个有
- `easy convertAnything` —— 2/5 个有
- `DF_Float` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
