---
name: unknown_workflow_sampler_clip_unet_77
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.97725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen image 酷炫锥形电影海报_1954123988979085313.json, 图片生成/文生图/qwen-image_1959137346446897153.json, 图片生成/文生图/qwen-image文生图工笔画关羽_1953057914565103617.json, 图片生成/文生图/qwen-image文生图珐琅彩孙悟空_1953757506445213698.json, 图片生成/文生图/qwen-image文生图青花瓷黛玉_1953758140024147969.json, 图片生成/文生图/qwen-通义千问-文生图_1952737054142697473.json, 图片生成/文生图/qwen_image_2512_bf16_2006410696564674562.json, 图片生成/文生图/turbo蒸馏版Z_IMAGE文生图工作流_2068265351833546753.json, 图片生成/文生图/z-image 8步生图_2041209465986355201.json, 图片生成/文生图/z-image工作流原始_1998312568252981249.json, 图片生成/文生图/z-image测试_2014249552764739586.json, 图片生成/文生图/z-image测试_2014252003039387649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/qwen image 酷炫锥形电影海报_1954123988979085313.json、图片生成/文生图/qwen-image_1959137346446897153.json、图片生成/文生图/qwen-image文生图工笔画关羽_1953057914565103617.json、图片生成/文生图/qwen-image文生图珐琅彩孙悟空_1953757506445213698.json、图片生成/文生图/qwen-image文生图青花瓷黛玉_1953758140024147969.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
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
- `PathchSageAttentionKJ` —— 3/12 个有
- `TextInputBasic` —— 2/12 个有
- `CR Value` —— 1/12 个有
- `ConcatTextOfUtils` —— 1/12 个有
- `LayerUtility: TextBox` —— 1/12 个有
- `YC_SingleTextNode` —— 1/12 个有
- `YC_textReplaceNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 12 | 36% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 12 | 47% |
| 采样算法 | euler | - | 12 | 75% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 0.81 - 1 | 12 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，12 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，12 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，12 个样本，一致性 75%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 0.81 - 1，12 个样本，取值集中（一致性 95%）
