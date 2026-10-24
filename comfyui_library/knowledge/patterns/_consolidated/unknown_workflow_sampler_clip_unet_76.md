---
name: unknown_workflow_sampler_clip_unet_76
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.696917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2512文生图_2053316351783124994.json, 图片生成/文生图/Qwen Image BF16满血版_1954768333373620226.json, 图片生成/文生图/Qwen Image fp8蒸馏版_1954773431147479041.json, 图片生成/文生图/Qwen Image 港风霓虹街景_2058558846393741314.json, 图片生成/文生图/Qwen image文生图Comfy fp8加速版本_1954314194239811586.json, 图片生成/文生图/Qwen image文生图Comfy官方fp8加lora版本_1954743795998965761.json, 图片生成/文生图/Qwen image文生图Comfy官方fp8版本_1952659040263421954.json, 图片生成/文生图/Qwen-image文生图 FP8 RAPID_1955920019513376770.json, 图片生成/文生图/Qwen2512测试工作流_2041793002967928833.json, 图片生成/文生图/image_qwen_image_2099207941726498817.json, 图片生成/文生图/image_z_image_2099207955014053890.json, 图片生成/文生图/爱小墨-图片-文生图-综合生成v1.0_2077346986138882050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_76

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2512文生图_2053316351783124994.json、图片生成/文生图/Qwen Image BF16满血版_1954768333373620226.json、图片生成/文生图/Qwen Image fp8蒸馏版_1954773431147479041.json、图片生成/文生图/Qwen Image 港风霓虹街景_2058558846393741314.json、图片生成/文生图/Qwen image文生图Comfy fp8加速版本_1954314194239811586.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 6/12 个有
- `PrimitiveBoolean` —— 6/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `PrimitiveFloat` —— 5/12 个有
- `LoraLoader` —— 3/12 个有
- `AV_LoraLoader` —— 2/12 个有
- `ResolutionSelector` —— 2/12 个有
- `PreviewImage` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `StringFormat` —— 1/12 个有
- `easy seed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 50 | 12 | 41% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 12 | 43% |
| 采样算法 | euler | - | 12 | 67% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 50，12 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，12 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
