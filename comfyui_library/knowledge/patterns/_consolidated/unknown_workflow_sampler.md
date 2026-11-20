---
name: unknown_workflow_sampler
type: Unknown Workflow
frequency: 31
level: strong
coverage: 0.868968
common_nodes: [CreateVideo, DiffuEraserLoader, DiffuEraserSampler, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [平台全量/即梦seedance2.0字幕去除（横屏16：9）_2035390193074708481.json, 平台全量/即梦超能视频2.0字幕去除（竖屏9：16）_2035450863422021633.json, 平台全量/即梦（ 9 ：16 竖版 ） SeeDance2 视频水印去除 + 高清化_2022511606239862786.json, 平台全量/去水印16_9横版-即梦超能视频2.0横版-视频局部去除+高清化_2021210124999725058.json, 平台全量/小云雀seedance2.0水印去除+高清化（16 _ 9 横板）_2020691299023720449.json, 平台全量/小云雀seedance2.0水印去除+高清化（9_16竖版）_2020662365045399554.json, 平台全量/视频去水印 16_9横版 固定去水印左上角和右下角_2096562554670764034.json, 平台全量/视频去水印 16_9横版 豆包即梦固定去水印左上角和右下角_2096596604080967682.json, 平台全量/视频去水印_2059919353201643522.json, 平台全量/视频去水印：竖版_2069391598294749186.json, 平台全量/视频水印去除+高清化 （自由修改版）_2021861491762270210.json, 平台全量/豆包1：1去水印_2070010966678532098.json, 平台全量/豆包eedance2.0视频去三水印-（9_16竖版）_2036629403286904833.json, 平台全量/豆包视频去水印16_9手动遮罩版_2029469741718446081.json, 平台全量/豆包视频去水印16_9手动遮罩版_2080931215611351041.json, 平台全量/超能视频2.0去水印_1996439954966323201.json, 平台全量/随变视频水印去除+高清化V2（9_16竖版）_2021775519292854273.json, 平台全量/（动态版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2021165391262785537.json, 平台全量/（动态版）豆包官方版seedance2.0水印去除+高清化V3（9_16竖版）_2024885131164520449.json, 平台全量/（动态版）豆包官方版超能视频2.0水印去除+高清化V3（16_9横版）_2024886831573110785.json, 平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（16_9横版）_2020109483384512514.json, 平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2020099631526453249.json, 平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（16_9横版）_2020102549113675777.json, 平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（9_16竖版）_2020111076595081217.json, 平台全量/（随变）seedance2.0水印去除+高清化V3（9_16竖版）_2021669365162188801.json, 平台全量/（随变）seedance2.0水印去除+高清化V3（9_16竖版）_2030827490515623937.json, 数字人/数字人/即梦官方版seedance2.0水印去除+高清化V2（16_9横版）_2020194791643947010.json, 数字人/数字人/小云雀seedance2.0水印去除+高清化V2（16_9横版）_2020301691408617474.json, 数字人/数字人/小云雀seedance2.0水印去除+高清化V2（9_16竖版）_2020200908319100929.json, 视频生成/图生视频/4.19横版16_9豆包官方版seedance2.0水印去除+高清化V3_2045784226385104897.json, 视频生成/图生视频/即梦官方版seedance2.0水印去除+高清化V2（9_16竖版）_2020315533945606146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（平台全量/即梦seedance2.0字幕去除（横屏16：9）_2035390193074708481.json、平台全量/即梦超能视频2.0字幕去除（竖屏9：16）_2035450863422021633.json、平台全量/即梦（ 9 ：16 竖版 ） SeeDance2 视频水印去除 + 高清化_2022511606239862786.json、平台全量/去水印16_9横版-即梦超能视频2.0横版-视频局部去除+高清化_2021210124999725058.json、平台全量/小云雀seedance2.0水印去除+高清化（16 _ 9 横板）_2020691299023720449.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 31 个 workflow 都包含：
- `CreateVideo`
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 30/31 个有
- `VHS_VideoCombine` —— 30/31 个有
- `LayerUtility: PurgeVRAM V2` —— 29/31 个有
- `MathExpression|pysssss` —— 29/31 个有
- `ImageConcanate` —— 26/31 个有
- `SaveImage` —— 23/31 个有
- `SaveVideo` —— 23/31 个有
- `CustomAddLabel` —— 7/31 个有
- `FlashVSRNode` —— 2/31 个有
- `MathExpression_UTK` —— 2/31 个有
- `PrimitiveFloat` —— 2/31 个有
- `AddMask` —— 1/31 个有
- `AnyBooleanSwitch` —— 1/31 个有
- `Masks Combine Regions` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.14472e+09 | 1.93653e+08 - 2.14507e+09 | 31 | 51% |
| Prompt 约束强度(CFG) | randomize | - | 31 | 94% |
| 采样算法 | 2 | 2 - 2 | 31 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 31 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 31 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.14472e+09，观测区间 1.93653e+08 - 2.14507e+09，31 个样本
- Prompt 约束强度(CFG) 最常用 randomize，31 个样本，一致性 94%
- 采样算法 中位数 2，观测区间 2 - 2，31 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，31 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，31 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.14507e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
