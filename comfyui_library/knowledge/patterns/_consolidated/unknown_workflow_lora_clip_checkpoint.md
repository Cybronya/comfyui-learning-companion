---
name: unknown_workflow_lora_clip_checkpoint
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.836875
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, SaveVideo, VRAMReserver, image_scale_pixel_v2]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039873152599203841.json, 视频生成/图生视频/LTX 2.3蒸馏1.1 + VBVR 逻辑优化-图生视频_2046866167066791938.json, 视频生成/图生视频/VBVR图生视频_2058031374677925889.json, 视频生成/图生视频/最新图生视频LTX 2.3-1.1 + VBVR_2045091410172452865.json, 视频生成/文生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039686946766721026.json, 视频生成/文生视频/LTX 2.3-1.1 + VBVR 图生视频_2045068954359570434.json, 视频生成/文生视频/VBVR图生视频_2043983814732550145.json, 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039873152599203841.json、视频生成/图生视频/LTX 2.3蒸馏1.1 + VBVR 逻辑优化-图生视频_2046866167066791938.json、视频生成/图生视频/VBVR图生视频_2058031374677925889.json、视频生成/图生视频/最新图生视频LTX 2.3-1.1 + VBVR_2045091410172452865.json、视频生成/文生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039686946766721026.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveVideo`
- `VRAMReserver`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 6/8 个有
- `Seed Everywhere` —— 6/8 个有
- `workflow>9958` —— 6/8 个有
- `workflow>515` —— 2/8 个有
- `workflow>675` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
