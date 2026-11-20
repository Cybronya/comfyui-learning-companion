---
name: unknown_workflow_generic_481
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.874167
common_nodes: [LoadImage, SaveImage, SeeThrough_GenerateDepth, SeeThrough_GenerateLayers, SeeThrough_LoadDepthModel, SeeThrough_LoadLayerDiffModel, SeeThrough_PostProcess, SeeThrough_SavePSD]
problems: []
missing: []
members: [图片生成/图生图/图层拆分psd格式-seetrough_2042442597188243458.json, 图片生成/图生图/新开源技术 seethrough-动漫人物图层拆分 林耀4.4_2040130396179931138.json, 图片生成/图生图/（工具流）live2D工具-SeeThrough-二次元人物单图PSD分层、拆图_2041062596421357570.json, 图片生成/文生图/seethrough-动漫人物图层拆分_2073317814898876418.json, 图片生成/文生图/图像分层  PSD  SeeThrough +全节点注释_2055168944914345985.json, 视频生成/图生视频/图像分层  PSD_2051130633145073665.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_481

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/图层拆分psd格式-seetrough_2042442597188243458.json、图片生成/图生图/新开源技术 seethrough-动漫人物图层拆分 林耀4.4_2040130396179931138.json、图片生成/图生图/（工具流）live2D工具-SeeThrough-二次元人物单图PSD分层、拆图_2041062596421357570.json、图片生成/文生图/seethrough-动漫人物图层拆分_2073317814898876418.json、图片生成/文生图/图像分层  PSD  SeeThrough +全节点注释_2055168944914345985.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeeThrough_GenerateDepth`
- `SeeThrough_GenerateLayers`
- `SeeThrough_LoadDepthModel`
- `SeeThrough_LoadLayerDiffModel`
- `SeeThrough_PostProcess`
- `SeeThrough_SavePSD`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/6 个有
- `PreviewImage` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
