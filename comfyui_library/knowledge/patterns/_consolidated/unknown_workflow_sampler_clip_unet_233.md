---
name: unknown_workflow_sampler_clip_unet_233
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.569167
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, KSampler, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MOSS单采_双采合集工作流_2112898314982215681.json, 图片生成/文生图/Qwen Image 2512文生图_2053316351783124994.json, 图片生成/文生图/Qwen Image 港风霓虹街景_2058558846393741314.json, 图片生成/文生图/Qwen2512测试工作流_2041793002967928833.json, 图片生成/文生图/image_qwen_image_2099207941726498817.json, 图片生成/文生图/image_z_image_2099207955014053890.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_233

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/MOSS单采_双采合集工作流_2112898314982215681.json、图片生成/文生图/Qwen Image 2512文生图_2053316351783124994.json、图片生成/文生图/Qwen Image 港风霓虹街景_2058558846393741314.json、图片生成/文生图/Qwen2512测试工作流_2041793002967928833.json、图片生成/文生图/image_qwen_image_2099207941726498817.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `ResolutionSelector` —— 3/6 个有
- `SetNode` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 20 - 50 | 5 | 65% |
| Prompt 约束强度(CFG) | 4 | 4 - 50 | 6 | 0% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 20 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 50，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
