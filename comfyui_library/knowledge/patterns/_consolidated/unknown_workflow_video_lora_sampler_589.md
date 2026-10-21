---
name: unknown_workflow_video_lora_sampler_589
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.562
common_nodes: [BasicScheduler, BerniniStudio, CLIPLoader, GetNode, INTConstant, Int, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SamplerCustom, Seed (rgthree), SetNode, SimpleMath+, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2076512997073313793.json, 视频生成/图生视频/2079802404345827330.json, 视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_589

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2076512997073313793.json、视频生成/图生视频/2079802404345827330.json、视频生成/文生视频/Berinini Studio x Remix LoRA 图生视频工作流_2079090473137950721.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `BerniniStudio`
- `CLIPLoader`
- `GetNode`
- `INTConstant`
- `Int`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SamplerCustom`
- `Seed (rgthree)`
- `SetNode`
- `SimpleMath+`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
