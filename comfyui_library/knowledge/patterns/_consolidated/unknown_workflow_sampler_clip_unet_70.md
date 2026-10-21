---
name: unknown_workflow_sampler_clip_unet_70
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.845889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/image_z_image_2099207955014053890.json, 图片生成/文生图/z_image-文生图_2018374992529985537.json, 图片生成/文生图/z_image_turbo_gap_focus_2015970628842557442.json, 图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json, 图片生成/文生图/z_image_turbo_飞速写实文生图_1994300683828527106.json, 图片生成/文生图/快速文生图：Z-image_zimage_2019318395178586113.json, 图片生成/文生图/文生图Qwen-Image-10步蒸馏_2018607735310393346.json, 图片生成/文生图/极致写实-Z-image-base-文生图_2017086284610670594.json, 图片生成/文生图/爱小墨-图片-文生图-综合生成v1.0_2077346986138882050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_70

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/image_z_image_2099207955014053890.json、图片生成/文生图/z_image-文生图_2018374992529985537.json、图片生成/文生图/z_image_turbo_gap_focus_2015970628842557442.json、图片生成/文生图/z_image_turbo_ultra_fast_1994239876770054145.json、图片生成/文生图/z_image_turbo_飞速写实文生图_1994300683828527106.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `CustomAddLabel` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `ResolutionSelector` —— 1/9 个有
- `StringFormat` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 50 | 9 | 31% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 8 | 9 | 21% |
| 采样算法 | res_multistep | - | 9 | 56% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 50，9 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 8，9 个样本，取值分散，一致性仅 21%
- 采样算法 最常用 res_multistep，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
