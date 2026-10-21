---
name: unknown_workflow_lora_sampler_unet_87
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.806
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, SelfLiftAvatarH3Sampler, SelfLiftAvatarH3TST, SolAttnMiniMax, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/7分钟直出1080P！12GB可用_BUNNY_SelfLift_高动态+LORA不模糊_混合工作流_2102283144824184833.json, 视频生成/文生视频/7分钟直出1080P！12GB可用_BUNNY_SelfLift_高动态+LORA不模糊_混合工作流_2102283144824184833.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_87

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/7分钟直出1080P！12GB可用_BUNNY_SelfLift_高动态+LORA不模糊_混合工作流_2102283144824184833.json、视频生成/文生视频/7分钟直出1080P！12GB可用_BUNNY_SelfLift_高动态+LORA不模糊_混合工作流_2102283144824184833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftAvatarH3Sampler`
- `SelfLiftAvatarH3TST`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
