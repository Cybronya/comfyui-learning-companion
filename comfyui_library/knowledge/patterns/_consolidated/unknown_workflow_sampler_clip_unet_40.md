---
name: unknown_workflow_sampler_clip_unet_40
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.956583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image最新千问文生图_1993894546499108866.json, 图片生成/文生图/Z-image 来袭，这才是真正的降维打击！_1994248474698989570.json, 图片生成/文生图/Z_image_turbo_文生图_1998723273162641410.json, 图片生成/文生图/Z_image_turbo即梦生图免费版_1998032212584988673.json, 图片生成/文生图/Z_image_turbo工作流_1994234495897452546.json, 图片生成/文生图/Z_image文生图标准版_2064278139861299201.json, 图片生成/文生图/image_ovis_文生图_1998947182181015554.json, 图片生成/文生图/qwen_image_2512_bf16_2006410696564674562.json, 图片生成/文生图/turbo蒸馏版Z_IMAGE文生图工作流_2068265351833546753.json, 图片生成/文生图/z-image工作流原始_1998312568252981249.json, 图片生成/文生图/z-image测试_2014249552764739586.json, 图片生成/文生图/z-image测试_2014252003039387649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z-Image最新千问文生图_1993894546499108866.json、图片生成/文生图/Z-image 来袭，这才是真正的降维打击！_1994248474698989570.json、图片生成/文生图/Z_image_turbo_文生图_1998723273162641410.json、图片生成/文生图/Z_image_turbo即梦生图免费版_1998032212584988673.json、图片生成/文生图/Z_image_turbo工作流_1994234495897452546.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 11/12 个有
- `Int` —— 2/12 个有
- `TextInputBasic` —— 2/12 个有
- `CR Value` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `easy getNode` —— 1/12 个有
- `easy setNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 50 | 12 | 17% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 12 | 20% |
| 采样算法 | euler | - | 12 | 67% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 50，12 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，12 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（9/12 个样本）：Steps较低可能导致细节不足
