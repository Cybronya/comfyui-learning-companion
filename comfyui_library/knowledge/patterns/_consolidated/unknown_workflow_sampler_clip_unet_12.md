---
name: unknown_workflow_sampler_clip_unet_12
type: Unknown Workflow
frequency: 34
level: strong
coverage: 0.940441
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2_2091139981032116226.json, 图片生成/文生图/Flux2_klein_2066878263074582530.json, 图片生成/文生图/Flux2_加速版文生图_1994696388929785858.json, 图片生成/文生图/Flux2‑Klein‑9B 文生图优化版_2086811458842750977.json, 图片生成/文生图/Flux2加速版文生图_1994007368916811777.json, 图片生成/文生图/Flux2文生图加速版V2(加强版)_1993501337226772482.json, 图片生成/文生图/俯视户外Flux2-Klein文生图真实人像质感御姐美女_2041474365199486977.json, 图片生成/文生图/古风美女Flux2-Klein文生图真实人像质感御姐美女_2042569677624315906.json, 图片生成/文生图/吊带睡衣Flux2-Klein文生图真实人像质感御姐美女_2041455000374747138.json, 图片生成/文生图/吊带睡衣Flux2-Klein文生图真实人像质感御姐美女_2041490972344848385.json, 图片生成/文生图/嘟嘟-Flux2文生图加速版_1994338243791486978.json, 图片生成/文生图/城市夜景Flux2-Klein文生图真实人像质感御姐美女_2042547795516727297.json, 图片生成/文生图/外国比基尼Flux2-Klein真实人像质感御姐美女_2041444521753448449.json, 图片生成/文生图/外国泳衣Flux2-Klein文生图真实人像质感御姐美女_2041446376365625346.json, 图片生成/文生图/婚纱美女Flux2-Klein文生图真实人像质感御姐美女_2042553118738616322.json, 图片生成/文生图/学生妹Flux2-Klein文生图真实人像质感御姐美女_2042566643066347521.json, 图片生成/文生图/居家美女Flux2-Klein文生图真实人像质感御姐美女_2042601666091950081.json, 图片生成/文生图/巷子印花Flux2-Klein文生图真实人像质感御姐美女_2042604254099152897.json, 图片生成/文生图/异域风情Flux2-Klein文生图真实人像质感御姐美女_2042469719067860994.json, 图片生成/文生图/性感女讲师Flux2-Klein文生图真实人像质感御姐美女_2042584107560996865.json, 图片生成/文生图/性感有韵味Flux2-Klein文生图真实人像质感御姐美女_2042577601297911809.json, 图片生成/文生图/成熟有气质Flux2-Klein文生图真实人像质感御姐美女_2041497010087403522.json, 图片生成/文生图/旗袍系列Klein文生图真实人像质感御姐美女_2051608959815041025.json, 图片生成/文生图/昏暗灯光Flux2-Klein文生图真实人像质感御姐美女_2041859831337848834.json, 图片生成/文生图/晚礼服Flux2-Klein文生图真实人像质感御姐美女_2041856183404859393.json, 图片生成/文生图/欧式美女Flux2-Klein文生图真实人像质感御姐美女_2041498188263198722.json, 图片生成/文生图/泳装系列Flux2-image真实人像质感御姐美女_2041434448171900929.json, 图片生成/文生图/漏脐短裤Flux2-Klein文生图真实人像质感御姐美女_2041453028020064258.json, 图片生成/文生图/睡衣系列Flux2-Klein真实人像质感御姐美女_2041443180914151426.json, 图片生成/文生图/立体立绘Flux2-Klein文生图真实人像质感御姐美女_2042587080278155265.json, 图片生成/文生图/粉色头发Flux2-Klein文生图真实人像质感御姐美女_2042599237376020481.json, 图片生成/文生图/美女写真图Flux2-Klein文生图真实人像质感御姐美女_2041492855360856065.json, 图片生成/文生图/蕾丝内衣Flux2-Klein文生图真实人像质感御姐美女_2041472519328243714.json, 图片生成/文生图/阳台东方美女Flux2-Klein文生图真实人像质感御姐美女_2041499725353979905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（图片生成/文生图/Flux2_2091139981032116226.json、图片生成/文生图/Flux2_klein_2066878263074582530.json、图片生成/文生图/Flux2_加速版文生图_1994696388929785858.json、图片生成/文生图/Flux2‑Klein‑9B 文生图优化版_2086811458842750977.json、图片生成/文生图/Flux2加速版文生图_1994007368916811777.json…）

- **类型**：Unknown Workflow
- **样本数**：34
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 34 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 33/34 个有
- `PathchSageAttentionKJ` —— 33/34 个有
- `EasyCache` —— 30/34 个有
- `LayerUtility: PurgeVRAM` —— 30/34 个有
- `CR Text` —— 29/34 个有
- `LoraLoaderModelOnly` —— 27/34 个有
- `FluxGuidance` —— 2/34 个有
- `Text _O` —— 2/34 个有
- `PrimitiveStringMultiline` —— 1/34 个有
- `UnetLoaderGGUF` —— 1/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 34 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 34 | 100% |
| 采样算法 | euler | - | 34 | 100% |
| 调度器 | simple | - | 34 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 34 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/34 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，34 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，34 个样本，一致性 100%
- 调度器 最常用 simple，34 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）
