---
name: unknown_workflow_sampler_unet_vae_71
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.81875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3  文生视频工作流_2084912279681851394.json, 视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-文生视频-自动提示词_2084463867618488321.json, 视频生成/文生视频/MiniMax H3 T2V comfyorg_2084874841076887553.json, 视频生成/文生视频/MiniMax H3 lightx2v 4步加速文生视频工作流_2086325686846976002.json, 视频生成/文生视频/MiniMax H3 加速版 文生视频_2086639037351284737.json, 视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json, 视频生成/文生视频/MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929.json, 视频生成/文生视频/MiniMax H3_文生视频工作流_2084504955460866050.json, 视频生成/文生视频/MiniMax H3文生视频工作流_2084632853681369090.json, 视频生成/文生视频/Minimax H3 FL2VA 图片首尾帧视频_2095354444597784577.json, 视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_71

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3  文生视频工作流_2084912279681851394.json、视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json、视频生成/文生视频/MiniMax H3 FL2VA开源版-文生视频-自动提示词_2084463867618488321.json、视频生成/文生视频/MiniMax H3 T2V comfyorg_2084874841076887553.json、视频生成/文生视频/MiniMax H3 lightx2v 4步加速文生视频工作流_2086325686846976002.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `PathchSageAttentionKJ` —— 7/12 个有
- `LoadImage` —— 4/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `MiniMaxH3BlockCacheT8` —— 3/12 个有
- `Text` —— 3/12 个有
- `VHS_VideoCombine` —— 3/12 个有
- `SpectrumSDXL` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `LoraLoaderBypassModelOnly` —— 1/12 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/12 个有
- `PainterVRAM` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
