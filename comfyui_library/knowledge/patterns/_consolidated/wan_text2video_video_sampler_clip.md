---
name: wan_text2video_video_sampler_clip
type: Wan Text2Video
frequency: 3
level: strong
coverage: 0.4
common_nodes: [CLIPTextEncode, UNETLoader, VHS_VideoCombine, WanVideoDecode, WanVideoSampler]
problems: [未检测到VAEDecode节点图像将无法解码]
missing: [WanVideoSampler, WanVideoDecode]
members: [wan_t2v_0.json, wan_t2v_1.json, wan_t2v_2.json]
source: knowledge_consolidation
---

# wan_text2video_video_sampler_clip

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（wan_t2v_0.json、wan_t2v_1.json、wan_t2v_2.json）

- **类型**：Wan Text2Video
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：40%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `UNETLoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSampler`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 5 | 5 - 6 | 3 | 91% |
| 采样步数 | 55 | 50 - 60 | 3 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 未检测到VAEDecode节点图像将无法解码 | 1/3 | low | 未检测到 VAEDecode 节点，图像将无法解码 → 添加 VAEDecode |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 6，3 个样本，取值集中（一致性 91%）
- 采样步数 中位数 55，观测区间 50 - 60，3 个样本，取值集中（一致性 93%）
- 这些节点还没有知识卡，系统对它们的理解有限：WanVideoSampler、WanVideoDecode
