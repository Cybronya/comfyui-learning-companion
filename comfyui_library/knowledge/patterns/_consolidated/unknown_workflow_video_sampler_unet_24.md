---
name: unknown_workflow_video_sampler_unet_24
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.486154
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085602340672987137.json, 视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json, 视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json, 视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2092541585006354433.json, 视频生成/文生视频/MiniMax H3 手机取物换装 文生视频_2106940320041750529.json, 视频生成/文生视频/MiniMax H3 文生视频_2090311300034424833.json, 视频生成/文生视频/MiniMax H3(全能多图参考生视频)4步Lora超级加速版_2085360950907064321.json, 视频生成/文生视频/MiniMax+H3  9 图_2085645558315831298.json, 视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json, 视频生成/文生视频/官方 全能参考版单采_2104530172652380161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_24

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085602340672987137.json、视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json、视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json、视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json、视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `PrimitiveFloat` —— 11/13 个有
- `Text` —— 10/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `MiniMaxH3ImageToVideo` —— 9/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/13 个有
- `LoadImage` —— 7/13 个有
- `Label (rgthree)` —— 5/13 个有
- `MiniMaxH3ReferenceToVideo` —— 4/13 个有
- `Fast Groups Bypasser (rgthree)` —— 3/13 个有
- `Float` —— 2/13 个有
- `MiniMaxH3SigmaShift` —— 2/13 个有
- `ModelAttentionBackend` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `SigmasGraph` —— 2/13 个有
- `AudioSeparation` —— 1/13 个有
- `CR Prompt Text` —— 1/13 个有
- `LoadAudio` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有
- `SplitSigmas` —— 1/13 个有
- `StringConcatenate` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
