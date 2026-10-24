---
name: unknown_workflow_lora_sampler_unet_69
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.691625
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/128.用Minimax H3+360度环绕lora+Skill做动态故事板，动态漫画，高级分镜视频_2109941253944201218.json, 图片生成/图生图/多角色对话丨MiniMax H3 Hybrid丨三图参考·音画同生_2112093052927037442.json, 视频生成/图生视频/H3_单采极速文戏_2106860537857527810.json, 视频生成/图生视频/H3_单采极速文戏_2109821779844886530.json, 视频生成/图生视频/H3_家庭储能广告_15秒_三图参考_2110987996991410177.json, 视频生成/图生视频/MiniMax H3 终极篇-文武双全_2110682294628474882.json, 视频生成/图生视频/minimax_H3_文戏工作流急速版_2107639659634454529.json, 视频生成/图生视频/改至YZ金鱼-MiniMax H3 终极篇-文武双全_2111027801062203393.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_69

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/128.用Minimax H3+360度环绕lora+Skill做动态故事板，动态漫画，高级分镜视频_2109941253944201218.json、图片生成/图生图/多角色对话丨MiniMax H3 Hybrid丨三图参考·音画同生_2112093052927037442.json、视频生成/图生视频/H3_单采极速文戏_2106860537857527810.json、视频生成/图生视频/H3_单采极速文戏_2109821779844886530.json、视频生成/图生视频/H3_家庭储能广告_15秒_三图参考_2110987996991410177.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 7/8 个有
- `LoadAudio` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `ModelPreviewOverrideKJ` —— 5/8 个有
- `SelfLiftH3Sampler` —— 5/8 个有
- `ExtendIntermediateSigmas` —— 4/8 个有
- `GetNode` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `Text` —— 4/8 个有
- `忽略多组孤海` —— 4/8 个有
- `BasicGuider` —— 3/8 个有
- `GoohaiUniversalSlider` —— 3/8 个有
- `PreviewAny` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `RandomNoise` —— 3/8 个有
- `SamplerCustomAdvanced` —— 3/8 个有
- `CreateVideo` —— 2/8 个有
- `EmptyImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LoraLoaderBypassModelOnly` —— 1/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/8 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/8 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/8 个有
- `easy loraStack` —— 1/8 个有
- `easy loraStackApply` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
