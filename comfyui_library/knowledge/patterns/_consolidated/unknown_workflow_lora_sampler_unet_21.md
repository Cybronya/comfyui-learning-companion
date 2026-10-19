---
name: unknown_workflow_lora_sampler_unet_21
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.895571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3 15秒卡点混剪工作流 像素幻想Lab_2090775624343445505.json, 视频生成/图生视频/Minimax H3 人物替换 单人极速版_2109840033103568897.json, 视频生成/图生视频/Minimax H3 人物替换 双人极速版_2109844433255620610.json, 视频生成/图生视频/Minimax-动作迁移_2086299017864114177.json, 视频生成/图生视频/MinimaxH3 4步加速故事板九宫格分镜多参考图视频工作流_2084506449723617282.json, 视频生成/文生视频/15秒卡点混剪_2092720568926818306.json, 视频生成/文生视频/3-MiniMax-H3-参考生视频工作流-V2_2084639172459065346.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3 15秒卡点混剪工作流 像素幻想Lab_2090775624343445505.json、视频生成/图生视频/Minimax H3 人物替换 单人极速版_2109840033103568897.json、视频生成/图生视频/Minimax H3 人物替换 双人极速版_2109844433255620610.json、视频生成/图生视频/Minimax-动作迁移_2086299017864114177.json、视频生成/图生视频/MinimaxH3 4步加速故事板九宫格分镜多参考图视频工作流_2084506449723617282.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `MuyeTextEditOutput` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `H3SigmaRefiner` —— 2/7 个有
- `VHS_VideoInfoLoaded` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `MiniMaxH3ContextIR` —— 1/7 个有
- `MiniMaxH3SigmaShift` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `VHS_LoadAudioUpload` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
