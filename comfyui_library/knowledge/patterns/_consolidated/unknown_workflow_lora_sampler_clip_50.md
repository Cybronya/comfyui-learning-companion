---
name: unknown_workflow_lora_sampler_clip_50
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.939875
common_nodes: [ApplyDreamO, CLIPTextEncode, DreamOProcessorLoader, DreamORefEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Dream o 真人穿动漫角色衣服_1929070963315609601.json, 图片生成/图生图/DreamO 官方急速版_1929981652209143809.json, 图片生成/图生图/DreamO-1.1单图参考_风格迁移_1938231620748906498.json, 图片生成/图生图/DreamO-1.1多图参考_风格一致性迁移_1938241613502283778.json, 图片生成/图生图/dreamo_comfyui_v1.1_1938194559962628097.json, 图片生成/图生图/【极速版】DreamO图像编辑（1分钟出图）_1930877725429399554.json, 图片生成/图生图/和拉布布合影-DreamO_1928569169275658241.json, 图片生成/文生图/DreamO官方10秒加速_IP&ID&Try-On和Style轻松搞定_字节开源服装一致性_1931254643706540033.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Dream o 真人穿动漫角色衣服_1929070963315609601.json、图片生成/图生图/DreamO 官方急速版_1929981652209143809.json、图片生成/图生图/DreamO-1.1单图参考_风格迁移_1938231620748906498.json、图片生成/图生图/DreamO-1.1多图参考_风格一致性迁移_1938241613502283778.json、图片生成/图生图/dreamo_comfyui_v1.1_1938194559962628097.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `ApplyDreamO`
- `CLIPTextEncode`
- `DreamOProcessorLoader`
- `DreamORefEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/8 个有
- `EmptySD3LatentImage` —— 5/8 个有
- `CR SDXL Aspect Ratio` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageScaleDownToSize` —— 1/8 个有
- `LayerUtility: TextBox` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 30 | 8 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
