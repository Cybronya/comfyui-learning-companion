---
name: unknown_workflow_video_upscale_latent_upscale_27
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.504167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3｜单人高质量数字人｜音频驱动多图参考 MV_2096969226736193537.json, 视频生成/图生视频/MiniMax_H3_去油腻_TwoPass_Ref2VA_2114214100938092545.json, 视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842.json, 视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2109548068579397633.json, 视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338.json, 视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102731516450263042.json, 视频生成/图生视频/Minimax-H3多参考双采放大生成视频（Singularity）_2096792911970136066.json, 视频生成/图生视频/MinimaxH3动作迁移-人物替换！完美优化_2110384977471954946.json, 视频生成/图生视频/MinimaxH3动作迁移-人物替换，完美优化_2114528770223857666.json, 视频生成/图生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版-9图全开_2099011685452439553.json, 视频生成/图生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版_2114647900906156034.json, 视频生成/图生视频/双倍高清放大MiniMax H3-多参考生视频-字节DMAD加速版_2106606807736209409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_27

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3｜单人高质量数字人｜音频驱动多图参考 MV_2096969226736193537.json、视频生成/图生视频/MiniMax_H3_去油腻_TwoPass_Ref2VA_2114214100938092545.json、视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842.json、视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2109548068579397633.json、视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `VAEDecodeAudio` —— 11/12 个有
- `VHS_LoadVideo` —— 11/12 个有
- `easy float` —— 11/12 个有
- `GetNode` —— 10/12 个有
- `SetNode` —— 10/12 个有
- `Text` —— 10/12 个有
- `忽略多组孤海` —— 9/12 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `Astra` —— 1/12 个有
- `CR Prompt Text` —— 1/12 个有
- `ImageFromBatch` —— 1/12 个有
- `Int` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LoadVideo` —— 1/12 个有
- `Lora Loader Stack (rgthree)` —— 1/12 个有
- `MiniMaxH3AVDecodeT8` —— 1/12 个有
- `ModelAttentionBackend` —— 1/12 个有
- `SaveAudioAdvanced` —— 1/12 个有
- `SaveVideo` —— 1/12 个有
- `SolAttnMiniMax` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `VRAM_Debug` —— 1/12 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/12 个有
- `easy showAnything` —— 1/12 个有
- `获取视频信息` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
