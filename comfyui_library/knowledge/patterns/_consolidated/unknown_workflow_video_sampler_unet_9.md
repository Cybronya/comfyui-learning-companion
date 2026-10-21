---
name: unknown_workflow_video_sampler_unet_9
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.561583
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2097993945132388353.json, 视频生成/图生视频/4-9宫图+Minimaxh3导演台（批量短剧专用）_2099703771608735745.json, 视频生成/图生视频/AI短剧制作全流程_2111223881188077570.json, 视频生成/图生视频/H3 动漫转真人+ 指定人物_2093180746625273857.json, 视频生成/图生视频/H3_动作迁移 + 深度视频参考_2090034137221648385.json, 视频生成/图生视频/MiNiMaxH3_六图+三音频参考_2111108549219799042.json, 视频生成/图生视频/MiniMax+H3-二采优化版_2102312716324130817.json, 视频生成/图生视频/MiniMax+H3-多参考生视频-优化版0909_2097580929232498689.json, 视频生成/图生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）二采_2109901185510629378.json, 视频生成/图生视频/MiniMax_H3-多参考生视频-_4步加速-一采二采双输出 工作流_2095689178364334082.json, 视频生成/图生视频/MiniMax_H3-多参考生视频-_4步加速-优化版_工作流_2095515551366991874.json, 视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2107829656270499842.json, 视频生成/图生视频/Minimax+H3 Turbo V4 + Realism peole 参考生视频超写实工作流_2109548068579397633.json, 视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102702993295630338.json, 视频生成/图生视频/Minimax-H3动作迁移2.0  史诗强化进阶版_2102731516450263042.json, 视频生成/图生视频/Minimax-H3多参考双采放大生成视频（Singularity）_2096792911970136066.json, 视频生成/图生视频/MinimaxH3动作迁移-人物替换！完美优化_2110384977471954946.json, 视频生成/图生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版-9图全开_2099011685452439553.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频_2097875587942666242.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频多比例版本_2104119164674859010.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2096460541328973825.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2097340280092581890.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒竖屏960分辨率）_2096477149321580546.json, 视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_9

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2097993945132388353.json、视频生成/图生视频/4-9宫图+Minimaxh3导演台（批量短剧专用）_2099703771608735745.json、视频生成/图生视频/AI短剧制作全流程_2111223881188077570.json、视频生成/图生视频/H3 动漫转真人+ 指定人物_2093180746625273857.json、视频生成/图生视频/H3_动作迁移 + 深度视频参考_2090034137221648385.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 23/24 个有
- `ComfyMathExpression` —— 22/24 个有
- `MiniMaxH3ReferenceToVideo` —— 22/24 个有
- `PrimitiveFloat` —— 22/24 个有
- `ResolutionSelector` —— 21/24 个有
- `Text` —— 20/24 个有
- `LoadAudio` —— 19/24 个有
- `VHS_LoadVideo` —— 19/24 个有
- `GetNode` —— 18/24 个有
- `LTXVConcatAVLatent` —— 18/24 个有
- `LTXVSeparateAVLatent` —— 18/24 个有
- `MinimaxH3LatentUpscaler3D` —— 18/24 个有
- `SetNode` —— 18/24 个有
- `SplitSigmas` —— 17/24 个有
- `忽略多组孤海` —— 16/24 个有
- `easy float` —— 15/24 个有
- `LoraLoaderModelOnly` —— 14/24 个有
- `ModelAttentionBackend` —— 10/24 个有
- `SolAttnMiniMax` —— 9/24 个有
- `Lora Loader Stack (rgthree)` —— 7/24 个有
- `Label (rgthree)` —— 4/24 个有
- `LoraLoaderBypassModelOnly` —— 4/24 个有
- `PrimitiveStringMultiline` —— 4/24 个有
- `孤海注释` —— 3/24 个有
- `INTConstant` —— 2/24 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/24 个有
- `PlaySound|pysssss` —— 2/24 个有
- `PrimitiveBoolean` —— 2/24 个有
- `SFH3MultimodalDirector` —— 2/24 个有
- `Fast Groups Bypasser (rgthree)` —— 1/24 个有
- `easy int` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
